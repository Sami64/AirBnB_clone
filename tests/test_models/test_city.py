#!/usr/bin/python3
""" Module for testing city"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_city(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_state_id(self):
        """Test state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)
