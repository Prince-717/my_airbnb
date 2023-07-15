#!/usr/bin/python3
"""
   TestFileStorage module
"""
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """
       The unittest module provides a rich set of tools for
    constructing and running tests
    """
    def test_instance(self):
        """
        if it's a FileStorage instance
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_obj_dict(self):
        """
        test object must be dictionary
        """
        value = storage.all()
        self.assertIsInstance(value, dict)

    def test_file_path(self):
        """
        check file path
        """
        file_path = FileStorage()._FileStorage__file_path
        self.assertIsInstance(file_path, str)

    def test_file_exists(self):
        """
        Test if file exist
        """
        self.assertTrue(os.path.exists("file.json"))

    def test_all(self):
        """
        Test all method
        """
        all_attributes = storage.all()
        self.assertIsInstance(all_attributes, dict)

    def test_new(self):
        """
        test new method
        """
        value = BaseModel()
        storage.new(value)
        obj_id = "BaseModel.{}".format(value.id)
        self.assertIn(obj_id, storage.all())

    def test_save(self):
        """
        test save method
        """
        storage.save()
        treload_1 = os.path.getsize(FileStorage._FileStorage__file_path)
        value = BaseModel()
        storage.new(value)
        storage.save()
        treload_2 = os.path.getsize(FileStorage._FileStorage__file_path)
        self.assertNotEqual(treload_1, treload_2)

    def test_reload_method(self):
        """
        test reload method
        """
        treload_1 = len(FileStorage._FileStorage__objects)
        storage.reload()
        treload_2 = len(FileStorage._FileStorage__objects)
        self.assertEqual(treload_1, treload_2)

    def test_save_2_datetime(self):
        """
        test 2 date not equal
        """
        date = BaseModel()
        update_time1 = date.updated_at
        update_time2 = datetime.now()

if __name__ == '__main__':
    unittest.main()
