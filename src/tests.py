import unittest

from funcs import (
    calculate_expression,
)


class TestValidateAndCalculateExpression(unittest.TestCase):
    def test_valid_expression_1(self):
        expr = "((3 + 5) * 2) - 6 / 2"
        result = calculate_expression(expr)
        self.assertEqual(result, 13.0)

    def test_valid_expression_2(self):
        expr = "1 + 2 * 5 - 10 / 2 + 10"
        result = calculate_expression(expr)
        self.assertEqual(result, 16.0)

    def test_valid_expression_3(self):
        expr = "1 + 2 * (3 - (4 / (5 + 1)))"
        result = calculate_expression(expr)
        self.assertEqual(result, 5.66)

    def test_negative_unary_expression(self):
        expr = "-100 - 10"
        result = calculate_expression(expr)
        self.assertEqual(result, -110)

    def test_decimal_expression(self):
        expr = "10.6 / 2.1"
        result = calculate_expression(expr)
        self.assertEqual(result, 5.04)

    def test_not_round_to_100ths(self):
        expr = "2 * (1 / 3)"
        result = calculate_expression(expr)
        self.assertNotEqual(result, 0.67)

    def test_positive_unary_expression(self):
        expr = "+10 + +20"
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_empty_brackets(self):
        expr = "() + 1"
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_unbalanced_parentheses(self):
        expr = "(3 + 5) * 2) - (6 / 2"
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_division_by_zero(self):
        expr = "5 / 0"
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_empty_expression(self):
        expr = ""
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_single_number_expression(self):
        expr = "50"
        with self.assertRaises(Exception):
            calculate_expression(expr)

    def test_missing_operator(self):
        expr = "5 (3 + 2)"
        with self.assertRaises(Exception):
            calculate_expression(expr)



if __name__ == "__main__":
    unittest.main()
