import unittest
from calculator_tool import calculator


class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.invoke(
            {"a": 25, "b": 48, "operation": "multiply"}), "1200.0")

    def test_add(self):
        self.assertEqual(calculator.invoke(
            {"a": 10, "b": 5, "operation": "add"}), "15.0")

    def test_division_by_zero(self):
        result = calculator.invoke(
            {"a": 10, "b": 0, "operation": "divide"})
        self.assertIn("division by zero", result.lower())

    def test_unsupported_operation(self):
        result = calculator.invoke(
            {"a": 10, "b": 5, "operation": "power"})
        self.assertIn("unsupported", result.lower())


if __name__ == "__main__":
    unittest.main()
