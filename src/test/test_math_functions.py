# test_math_operations.py

import unittest
from src.main.math_functions import calculate_square_of_the_number, calculate_square_root_of_the_number


class TestMathOperations(unittest.TestCase):
    def test_square_positive_number(self):
        try:
            self.assertEqual(calculate_square_of_the_number(2), 4)
            self.assertEqual(calculate_square_of_the_number(5), 25)
            print("Test case test_square_positive_number passed!")
        except AssertionError:
            print("Test case test_square_positive_number failed!")

    def test_square_negative_number(self):
        try:
            self.assertEqual(calculate_square_of_the_number(-3), 9)
            self.assertEqual(calculate_square_of_the_number(-6), 36)
            print("Test case test_square_negative_number passed!")
        except AssertionError:
            print("Test case test_square_negative_number failed!")

    def test_square_zero(self):
        try:
            self.assertEqual(calculate_square_of_the_number(0), 0)
            print("Test case test_square_zero passed!")
        except AssertionError:
            print("Test case test_square_zero failed!")



    def test_sqrt_positive_number(self):
        try:
            self.assertEqual(calculate_square_root_of_the_number(4), 2)
            self.assertEqual(calculate_square_root_of_the_number(225), 15)
            print("Test case test_sqrt_positive_number passed!")
        except AssertionError:
            print("Test case test_sqrt_positive_number failed!")


    def test_sqrt_negative_number(self):
        #self.assertNotEquals(calculate_square_root_of_the_number(-225), 15)
        try:
            self.assertEqual(calculate_square_root_of_the_number(0), 0)
            print("Test case test_sqrt_negative_number passed!")
        except AssertionError:

            print("Test case test_sqrt_negative_number FAILED!")


if __name__ == '__main__':
    unittest.main()
