#!/usr/bin/python3
"""Amenity module unittest."""
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Amenity(unittest.TestCase):
    """Amenity Class test """
    examplee = Amenity()

    def setUp(self):
        """Set up the testing for amenities"""
        FileStorage._FileStorage__file_path = "test.json"
        self.amenity = Amenity()
        self.amenity.name = "remarkable"
        self.amenity.save()

    def test_class_existance(self):
        """Tests if class is found"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.examplee)), result)

    def testpublic(self):
        self.assertEqual(str, type(Amenity().id))

    def test_instance_User(self):
        """Test BaseModel subclasses"""
        self.assertIsInstance(self.examplee, Amenity)

    def test_atrr_type_Amenity(self):
        """Test attribute for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_attribute_name(self):
        """Check name"""
        self.assertEqual(hasattr(self.examplee, "name"), True)

    def test_types(self):
        """Test types"""
        self.assertEqual(type(self.examplee.name), str)

    def testHasAttributes(self):
        """Verify if attributes are present"""
        self.assertTrue(hasattr(self.examplee, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.examplee, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
