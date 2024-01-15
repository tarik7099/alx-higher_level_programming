import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_id_increment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)
