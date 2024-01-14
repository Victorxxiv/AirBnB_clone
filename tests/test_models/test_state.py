#!/usr/bin/python3
"""State module unittest"""
import os
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_State(unittest.TestCase):
    """State Class test"""

    def setUp(self):
        """set, testing States"""
        FileStorage._FileStorage__file_path = "test.json"
        self.state = State()
        self.state.name = "Florida"
        self.state.save()

    def test_docstring_State(self):
        """Docstrings check"""
        self.assertIsNotNone(State.__doc__)

    def test_instance_State(self):
        """Valid type check"""
        self.assertTrue(type(self.state.name) is str)

    def test_to_dict_State(self):
        """Dictionary works test"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def testpublic(self):
        self.assertEqual(str, type(State().id))

    def testHasAttributes(self):
        """Attributes exist, verify"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
