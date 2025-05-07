import unittest
from Reggie_Linear_Regression import get_y, calculate_error, calculate_all_error
from data import test_datapoints


class TestGetY(unittest.TestCase):

    def test_basic_fucntionality(self):
        self.assertEqual(get_y(1, 0, 7), 7)

    def test_positive_slope(self):
        self.assertEqual(get_y(5, 10, 3), 25)

    def test_negative_slope(self):
        self.assertEqual(get_y(-3, 5, 2), -1)

    def test_Zero_slope(self):
        self.assertEqual(get_y(0, 10, 5), 10)


class TestCalculateError(unittest.TestCase):

    def test_zero_ditance(self):
        self.assertEqual(calculate_error(1, 0, (3, 3)), 0)

    def test_single_distance(self):
        self.assertEqual(calculate_error(1, 0, (3, 4)), 1)

    def test_negative_intercept(self):
        self.assertEqual(calculate_error(1, -1, (3, 3)), 1)

    def test_negative_slope(self):
        self.assertEqual(calculate_error(-1, 1, (3, 3)), 5)


class TestCalculateAllError(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(calculate_all_error(1, 0, test_datapoints), 0)

    def test_case_two(self):
        self.assertEqual(calculate_all_error(1, 1, test_datapoints), 4)

    def test_case_three(self):
        self.assertEqual(calculate_all_error(1, -1, test_datapoints), 4)

    def test_case_four(self):
        self.assertEqual(calculate_all_error(-1, 1, test_datapoints), 18)


unittest.main()
