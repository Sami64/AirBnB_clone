#!/usr/bin/python3
""" Module for testing Place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test max guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test longitude"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
