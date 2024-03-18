#!/usr/bin/python3
"""Testing... """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Testing... """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

   
    def test_user_id(self):
        """ Testing..."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Testing... """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_place_id(self):
        """Testing... """
        new = self.value()
        self.assertEqual(type(new.place_id), str)
