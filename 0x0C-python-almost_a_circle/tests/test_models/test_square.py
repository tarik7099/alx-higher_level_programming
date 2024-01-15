#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
"""
import os
import unittest
from models.square import Square

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 5")
