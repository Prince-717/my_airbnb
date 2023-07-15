#!/usr/bin/python3
"""
   TestCity module
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    TestCity class
    """
    def test_city_creation(self):
        """
        Test instance creation
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_variables(self):
        """
        test variables creation
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_id(self):
        """
        test unique id for city
        """
        city_id_1 = City()
        city_id_2 = City()
        self.assertNotEqual(city_id_1, city_id_2)

if __name__ == '__main__':
    unittest.main()
