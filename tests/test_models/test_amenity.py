#!/usr/bin/python3
"""module to test Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test for amenity class """

    def __init__(self, *args, **kwargs):
        """attribute for amenity class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """method of amenity test class """
        new = self.value()
        self.assertEqual(type(new.name), str)
