from math import floor
import re
from calculator.infix_to_postfix_converter import InfixToPostfixConverter
from calculator.postfix_evaluator import PostfixEvaluator

# Здесь используется алгоритм преобразования инфиксного выражения в постфиксное, с последующим вычислением значения
class Calculator:
    def __init__(self, expr: str, ndigits: int = 2):
        self.expr = expr
        self.ndigits = ndigits

    def calculate(self) -> float:
        if not self.expr:
            raise Exception("Пустое выражение")
        if not self._contains_math_operations(self.expr):
            raise ValueError("Выражение не содержит  математических операций")

        tokens = self._parse_tokens()

        converter = InfixToPostfixConverter(tokens)
        postfix_expr = converter.convert()

        evaluator = PostfixEvaluator(postfix_expr)
        result = evaluator.evaluate()

        return self._truncate(result, self.ndigits)

    def _parse_tokens(self):
        tokens = re.findall(r"-?\d+\.\d+|-?\d+|[+\-*/()]", self.expr)
        return tokens

    def _contains_math_operations(self, expr: str) -> bool:
        operators = set("+-*/")
        return any(op in expr for op in operators)

    def _truncate(self, f: float, n: int) -> float:
        return floor(f * 10**n) / 10**n
