#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest the max_integer function"""

    def test_equal(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(list(range(10))), 9)
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer([2, 5, 1, 2, 10]), 10)
        self.assertEqual(max_integer('Python is cool'), 'y')
        self.assertEqual(max_integer(['Python', 'is', 'cool']), 'is')
        self.assertEqual(max_integer([23.1, 34.2, 32.9, 3.2, 5]), 34.2)


if __name__ == "__main__":
    unittest.main()
