#!/usr/bin/python3
"""module to test place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """class to test place"""

    def __init__(self, *args, **kwargs):
        """attribute of class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """method of place test class"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
