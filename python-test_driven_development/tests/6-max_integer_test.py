#!/usr/bin/python3

"""This file contains the Unittests for 6-max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

def test_max_at_end(self):
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)
def test_max_at_beginning(self):
    self.assertEqual(max_integer([4, 3, 2, 1]), 4)
def test_max_in_middle(self):
    self.assertEqual(max_integer([1, 4, 2, 3]), 4)
def test_one_negative_number(self):
    self.assertEqual(max_integer([-5]), -5)
def test_only_negative_numbers(self):
    self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
def test_list_of_one_element(self):
    self.assertEqual(max_integer([7]), 7)
def test_list_is_empty(self):
    self.assertIsNone(max_integer([]))

if __name__ == "__main__":
    unittest.main()
