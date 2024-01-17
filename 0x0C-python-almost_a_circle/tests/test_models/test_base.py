#!/usr/bin/python3
import unittest
from models.base import Base
"""find module"""


class TestBase(unittest.TestCase):
    """class to test"""
    def test_id_increment(self):
        """method to test increment"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id(self):
        """method to test id with argument"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
