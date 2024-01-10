#!/usr/bin/python3

"""
Unittest for max_integer()
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_values(self):
        self.assertEqual(max_integer([-2, -5, -5, -10]), -2)
    
    def testzero(self):
        self.assertEqual(max_integer([-1, -6, -70, 0]), 0)

    def test_duplicate_values(self):
        """double """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        
    def testtrible(self):
        """ the max"""
        self.assertEqual(max_integer([1, 1, 1, 7, 1]), 7)

    def test_float_values(self):
        """more float"""
        self.assertEqual(max_integer([1.5, 3.3, 0.9, 6.5]), 6.5)
    
    def testfloet(self):
        """float"""
        self.assertEqual(max_integer([-1.5, -6.3, -0.9, -3.5]), -0.9)

    def test_mixed_values(self):
        """the max"""
        self.assertEqual(max_integer([1, 3.5, 3, 4]), 4)
    
    def testnega(self):
        """negative"""
        self.assertEqual(max_integer([-1, -2.5, -3, -4]), -1)
    
    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")
if __name__ == '__main__':
    unittest.main()
