import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/test/Unit Test Addition.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('/test/Unit Test Subtraction.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/test/Unit Test Multiplication.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

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
