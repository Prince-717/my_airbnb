#!/usr/bin/python3
"""
   TestReview module
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    TestReview class
    """
    def test_review_creation(self):
        """
        Test instance creation
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_variables(self):
        """
        test variables creation
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_id(self):
        """
        test unique id for review
        """
        review_id_1 = Review()
        review_id_2 = Review()
        self.assertNotEqual(review_id_1, review_id_2)

if __name__ == '__main__':
    unittest.main()
