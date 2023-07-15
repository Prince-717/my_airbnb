#!/usr/bin/python3
"""
TestUser module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
       TestUser class
    """

    def test_user_creation(self):
        """
        test instance creation
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_variables(self):
        """
        test variable creation
        """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_id(self):
        """
        test unique id
        """
        user_id_1 = User()
        user_id_2 = User()
        self.assertNotEqual(user_id_1, user_id_2)

if __name__ == '__main__':
    unittest.main()
