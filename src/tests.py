import unittest

from funcs import (
    validate_and_calculate_expression,
)


class TestValidateAndCalculateExpression(unittest.TestCase):
    def test_valid_expression_1(self):
        expr = "((3 + 5) * 2) - 6 / 2"
        result = validate_and_calculate_expression(expr)
        self.assertEqual(result, 14.0)

    def test_valid_expression_2(self):
        expr = "1 + 2 * 5 - 10 / 2 + 10"
        result = validate_and_calculate_expression(expr)
        self.assertEqual(result, 16.0)

    def test_valid_expression_3(self):
        expr = "1 + (2 * (3 - (4 / (5 + 1))))"
        result = validate_and_calculate_expression(expr)
        self.assertEqual(result, 2.83)

    def test_unbalanced_parentheses(self):
        expr = "(3 + 5) * 2) - (6 / 2"
        with self.assertRaises(ValueError):
            validate_and_calculate_expression(expr)

    def test_division_by_zero(self):
        expr = "5 / 0"
        with self.assertRaises(ZeroDivisionError):
            validate_and_calculate_expression(expr)

    def test_empty_expression(self):
        expr = ""
        with self.assertRaises(ValueError):
            validate_and_calculate_expression(expr)


if __name__ == "__main__":
    unittest.main()
