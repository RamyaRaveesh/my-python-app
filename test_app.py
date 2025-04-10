import unittest
from app import add, subtract, multiply, divide

class TestCalculatorApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(5, 0), "Error! Division by zero.")

if __name__ == '__main__':
    unittest.main()
