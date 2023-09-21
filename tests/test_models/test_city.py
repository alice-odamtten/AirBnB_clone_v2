#!/usr/bin/python3
"""module for city test"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """the city test class """

    def __init__(self, *args, **kwargs):
        """the attribute of the class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """method to test state"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """method to test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
