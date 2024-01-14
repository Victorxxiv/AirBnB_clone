#!/usr/bin/python3
"""City module unittest"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_City(unittest.TestCase):
    """City Class test"""

    def setUp(self):
        """set, testing cities"""
        FileStorage._FileStorage__file_path = "test.json"
        self.city = City()
        self.city.name = "Oslo"
        self.city.save()

    def test_attributes_City(self):
        """City have attributes, checked"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertEqual(hasattr(self.city, "name"), True)

    def test_instance_City(self):
        """Valid type, check"""
        self.assertTrue(type(self.city.name) is str)
        self.assertTrue(type(self.city.id) is str)

    def test_docstring_City(self):
        """Docstrings check"""
        self.assertIsNotNone(City.__doc__)

    def test_any_attribute(self):
        """Attributes existance, check"""
        self.assertEqual(hasattr(self.city, "state_id"), True)
        self.assertEqual(hasattr(self.city, "name"), True)

    def testpublic(self):
        self.assertEqual(str, type(City().id))

    def test_save_City(self):
        """Save works test"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
