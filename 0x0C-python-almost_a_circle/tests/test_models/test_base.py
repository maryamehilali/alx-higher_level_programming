#!/usr/bin/python3
"""tests for the class Base"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """suite tests for Base Class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """test for id default"""
        new = Base()
        self.assertEqual(new.id, 1)
        new2 = Base()
        self.assertEqual(new2.id, 2)

    def test_id_input(self):
        """test for id input user"""
        new = Base(5)
        self.assertEqual(new.id, 5)
        new2 = Base()
        self.assertEqual(new2.id, 1)

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)
            
    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
