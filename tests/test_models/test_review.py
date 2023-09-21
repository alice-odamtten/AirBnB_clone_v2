#!/usr/bin/python3
"""model to test review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """class to test review"""

    def __init__(self, *args, **kwargs):
        """attribute of test class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test the class review"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """method to test class review"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """method to test class review"""
        new = self.value()
        self.assertEqual(type(new.text), str)
