#!/usr/bin/python3

"""This file contains the Unittests for 6-max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

def test_max_at_end(self):
        """Test when the max integer is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)