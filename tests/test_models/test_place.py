#!/usr/bin/python3
"""
   TestPlace module
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    TestPlace class
    """
    def test_place_creation(self):
        """
        Test instance creation
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_variables(self):
        """
        test variables creation
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_id(self):
        """
        test unique id for place
        """
        place_id_1 = Place()
        place_id_2 = Place()
        self.assertNotEqual(place_id_1, place_id_2)

if __name__ == '__main__':
    unittest.main()
