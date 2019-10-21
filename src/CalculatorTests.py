import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_division(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square(self):
        self.assertEqual(self.calculator.square(3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(4), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
