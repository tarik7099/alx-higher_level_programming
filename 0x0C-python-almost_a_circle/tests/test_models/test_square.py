import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 5")
