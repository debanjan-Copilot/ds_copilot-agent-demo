import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import main


class CalculatorOperationTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(main.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(main.divide(8, 2), 4)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            main.divide(8, 0)


class NumericValidationTests(unittest.TestCase):
    def test_numeric_values_are_valid(self):
        self.assertTrue(main.is_numeric("12"))
        self.assertTrue(main.is_numeric("-3.5"))

    def test_non_numeric_values_are_invalid(self):
        self.assertFalse(main.is_numeric("hello"))
        self.assertFalse(main.is_numeric(""))


class CalculatorCliTests(unittest.TestCase):
    def run_calculator(self, inputs):
        output = io.StringIO()
        with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
            main.main()
        return output.getvalue()

    def test_calculates_result_and_quits(self):
        output = self.run_calculator(["6", "+", "4", "q"])

        self.assertIn("Result: 10.0", output)

    def test_rejects_non_numeric_first_input(self):
        output = self.run_calculator(["abc", "q"])

        self.assertIn("Error: Please enter a numeric value.", output)

    def test_rejects_non_numeric_second_input(self):
        output = self.run_calculator(["6", "+", "abc", "q"])

        self.assertIn("Error: Please enter a numeric value.", output)

    def test_rejects_invalid_operation(self):
        output = self.run_calculator(["6", "%", "q"])

        self.assertIn("Invalid operation.", output)

    def test_reports_division_by_zero(self):
        output = self.run_calculator(["6", "/", "0", "q"])

        self.assertIn("Error: Cannot divide by zero", output)


if __name__ == "__main__":
    unittest.main()
