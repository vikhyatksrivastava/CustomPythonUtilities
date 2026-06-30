import unittest
from src.main.lambda_titorial import add_ten, factorial_altered, factorial_with_temp

class TestLambdaFunctions(unittest.TestCase):
    def test_add_ten(self):
        self.assertEqual(add_ten(5), 15)
        self.assertEqual(add_ten(-10), 0)
        self.assertEqual(add_ten(0), 10)

    def test_factorial_altered(self):
        self.assertEqual(factorial_altered(5), 720 * 125) # 5! * 5^3
        self.assertEqual(factorial_altered(6), factorial_with_temp * 216) # 6! * 6^3