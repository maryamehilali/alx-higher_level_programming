#!/usr/bin/python3
"""tests for the class Rectangle"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """suite tests for Rectangle Class"""
    def test_rectangle1(self):
        """test new rectangle instance"""
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_rectangle2(self):
        """test new rectangle with id"""
        new = Rectangle(2, 4, 3, 4, 18)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.x, 3)
        self.assertEqual(new.y, 4)
        self.assertEqual(new.id, 18)

    def test_missing_args(self):
        """case of missing args"""
        with self.assertRaises(TypeError):
            new = Rectangle(2)
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_acces_private(self):
        """accessing private attributes"""
        new = Rectangle(2, 4, 2, 3, 25)
        with self.assertRaises(AttributeError):
            new.__width
        with self.assertRaises(AttributeError):
            new.__height
        with self.assertRaises(AttributeError):
            new.__x
        with self.assertRaises(AttributeError):
            new.__y
