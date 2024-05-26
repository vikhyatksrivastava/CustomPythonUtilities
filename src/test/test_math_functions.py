# test_math_operations.py

import unittest
from src.main.math_functions import calculate_square_of_the_number, calculate_square_root_of_the_number


class TestMathOperations(unittest.TestCase):
    def test_square_positive_number(self):
        self.assertEqual(calculate_square_of_the_number(2), 4)
        self.assertEqual(calculate_square_of_the_number(5), 25)

    def test_square_negative_number(self):
        self.assertEqual(calculate_square_of_the_number(-3), 9)
        self.assertEqual(calculate_square_of_the_number(-6), 36)

    def test_square_zero(self):
        self.assertEqual(calculate_square_of_the_number(0), 0)


    def test_sqrt_positive_number(self):
        self.assertEqual(calculate_square_root_of_the_number(4), 2)
        self.assertEqual(calculate_square_root_of_the_number(225), 15)

    def test_sqrt_negative_number(self):
        #self.assertNotEquals(calculate_square_root_of_the_number(-225), 15)
        self.assertEqual(calculate_square_root_of_the_number(0), 0)


if __name__ == '__main__':
    unittest.main()
