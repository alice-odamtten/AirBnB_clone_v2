#!/usr/bin/python3
"""model to test class state"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """class to test state"""

    def __init__(self, *args, **kwargs):
        """attribute of class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """method to test class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
