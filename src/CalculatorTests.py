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
        test_data = CsvReader('/test/Unit Test Division.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square(self):
        test_data = CsvReader('/test/Unit Test Square.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.squire(row['Value 1']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('/test/Unit Test Square Root.csv').data
        for row in test_data:
        self.assertEqual(self.calculator.squire_root(row['Value 1']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
