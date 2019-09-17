""" Author: Michael Harmon
    Last Date Modified: 09/16/2019
    Description: These unit tests with test the average()
    from average_scores.py
    Update: Add tests for ValueError
    Update: Modified test_average_negative_input
    to test score 2 raises value error
"""

import unittest
from unittest import mock
from input_validation import validation_with_try as v


class MyTestCase(unittest.TestCase):
    def test_average_positive(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert v.average() == 90

    def test_average_negative(self):
        with mock.patch('builtins.input', side_effect=[98, 93, 88]):
            assert v.average() != 91

    def test_average_string_raises_ValueError(self):
        with mock.patch('builtins.input', side_effect=['Test', 'Test', 'Test']):
            self.assertRaises(ValueError)

    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            v.average(96, -93, 88)


if __name__ == '__main__':
    unittest.main()

"""The unit tests ensured that the average method was actually returning the average.
    I added a positive test that returned the correct average and a negative test
    that would not return the correct average.
    This will ensure the average() method is calculating correctly.
"""
