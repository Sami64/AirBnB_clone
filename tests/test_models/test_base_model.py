#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Class for testing BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Setting up"""
        pass

    def tearDown(self):
        """Cleaning up after each test"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_default(self):
        """Testing default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Testing kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertEqual(type(new), self.value)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            i = self.value(**copy)

    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__))

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'Kevin', '__class__': 'BaseModel', 'updated_at': '2022-01-01T12:00:00.000000',
             'created_at': '2022-01-01T12:00:00.000000'}
        print(f"kwargs: {n}")
        print(f"self.value: {self.value}")
        with self.assertRaises(TypeError) as context:
            new = self.value(**n)
        self.assertEqual(str(context.exception), "Unexpected keyword argument(s) passed to BaseModel: 'Name'")

    def test_id(self):
        """ """
        i = self.value()
        self.assertEqual(type(i.id), str)

    def test_created_at(self):
        """ """
        i = self.value()
        self.assertEqual(type(i.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        i = self.value()
        self.assertEqual(type(i.updated_at), datetime.datetime)
        n = i.to_dict()
        i = BaseModel(**n)
        self.assertFalse(i.created_at == i.updated_at)
