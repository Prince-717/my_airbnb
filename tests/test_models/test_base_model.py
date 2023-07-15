#!/usr/bin/python3
""" TestBaseModel module for testing the BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
import os
import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel class """

    def test_id(self):
        """ test id """
        model_base_1 = BaseModel()
        model_base_2 = BaseModel()
        self.assertNotEqual(model_base_1.id, model_base_2.id)

    def test_str(self):
        """ test string """
        model_base = BaseModel()
        self.assertEqual(type(model_base.__str__()), str)

    def test_save(self):
        """ test save to json """
        self.assertTrue(os.path.exists("file.json"))

    def test_transformation_to_dict(self):
        """
        Tests to_dict method
        """
        model_base = BaseModel()
        model_base.name = "Betty"
        model_base.number = 89
        base_model = model_base.to_dict()
        time_created = model_base.created_at.isoformat()
        time_updated = model_base.updated_at.isoformat()
        model_base_id = model_base.id
        expected_dict = {
            "name": "Betty",
            "number": 89,
            "id": model_base_id,
            "__class__": "BaseModel",
            "created_at": time_created,
            "updated_at": time_updated
            }

    def test_to_dict(self):
        """ test attributes to dict """
        model_base = BaseModel()
        model_base.my_name = "ALX"
        model_base.my_number = 89
        base_to_json = model_base.to_dict()
        self.assertIsInstance(base_to_json["my_number"], int)
        self.assertIsInstance(base_to_json["my_name"], str)
        self.assertIsInstance(base_to_json["__class__"], str)
        self.assertIsInstance(base_to_json["updated_at"], str)
        self.assertIsInstance(base_to_json["created_at"], str)
        self.assertIsInstance(base_to_json["id"], str)

    def test_kwargs_instance(self):
        """
        test instance with multiple args
        """
        kwargs = {"name": "ALX", "number": 89}
        model_base = BaseModel(**kwargs)
        self.assertEqual(model_base.name, "ALX")
        self.assertEqual(model_base.number, 89)

if __name__ == '__main__':
    unittest.main()
