#!/usr/bin/python3
"""module to test user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """class to test user class"""

    def __init__(self, *args, **kwargs):
        """attribute test user class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """method to test user class"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """method to test user class"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """method to test user class"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """method to test user class"""
        new = self.value()
        self.assertEqual(type(new.password), str)
