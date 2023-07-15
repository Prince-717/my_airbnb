#!/usr/bin/python3
"""
   Test Amenity 
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class
    """
    def test_amenity_creation(self):
        """
        Test instance creation
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_variables(self):
        """
        Test creation of variables
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_id(self):
        """
        Test if id for amenity is unique
        """
        amenity_id_1 = Amenity()
        amenity_id_2 = Amenity()
        self.assertNotEqual(amenity_id_1, amenity_id_2)

if __name__ == '__main__':
    unittest.main()
