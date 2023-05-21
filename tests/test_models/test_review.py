#!/usr/bin/python3
""" Module for testing review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
