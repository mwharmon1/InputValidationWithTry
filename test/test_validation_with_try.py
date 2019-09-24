""" Author: Michael Harmon
    Last Date Modified: 09/23/2019
    Description: These unit tests with test the average()
    from average_scores.py
    Update: Add tests for ValueError
    Update: Added more tests to validate
    function raises value error for all 3 scores
    when negative. Using assert instead of mock because
    my function takes in 3 args so I don't need to mock them.
"""

import unittest
from unittest import mock
from input_validation import validation_with_try as v


class MyTestCase(unittest.TestCase):
    def test_average_positive(self):
        self.assertEqual(v.average(98, 93, 88), 93)

    def test_average_negative(self):
        self.assertNotEqual(v.average(100, 87, 91), 90)

    def test_average_negative_input_raises_value_error_score_1(self):
        self.assertRaises(ValueError, v.average, -99, 87, 91)

    def test_average_negative_input_raises_value_error_score_2(self):
        self.assertRaises(ValueError, v.average, 99, -84, 91)

    def test_average_negative_input_raises_value_error_score_3(self):
        self.assertRaises(ValueError, v.average, 100, 88, -97)


if __name__ == '__main__':
    unittest.main()

"""The unit tests ensured that the average method was actually returning the average.
    I added a positive test that returned the correct average and a negative test
    that would not return the correct average.
    This will ensure the average() method is calculating correctly.
    I also added tests to raise value error for all 3 scores when 
    they are negative.
"""
