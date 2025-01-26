#!/usr/bin/python3

"""This file contains the Unittests for 6-max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([7]), 7)
        self.assertIsNone(max_integer([]))

if __name__ == "__main__":
    unittest.main()