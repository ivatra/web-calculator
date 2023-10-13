import re
from math import floor


# Здесь используется алгоритм преобразования инфиксного выражения в постфиксное, с последующим вычислением значения
class Calculator:
    def __init__(self, expr: str, ndigits: int = 2):
        self.expr = expr
        self.ndigits = ndigits

    def calculate(self) -> float:
        if not self.expr:
            raise Exception("Пустое выражение")
        if not self._contains_math_operations(self.expr):
            raise ValueError(
                "Выражение не содержит  математических операций"
            )

        tokens = re.findall(r"-?\d+\.\d+|-?\d+|[+\-*/()]", self.expr)

        postfix_expr = self._infix_to_postfix(tokens)

        result = self._evaluate_postfix(postfix_expr)

        return self._truncate(result, self.ndigits)

    def _contains_math_operations(self, expr: str) -> bool:
        operators = set("+-*/")
        return any(op in expr for op in operators)

    def _truncate(self, f: float, n: int) -> float:
        return floor(f * 10**n) / 10**n

    def _get_operator_priority(self, operator) -> int:
        if operator in ["+", "-"]:
            return 1
        elif operator in ["*", "/"]:
            return 2
        return 0

    def _infix_to_postfix(self, tokens: str) -> list:
        stack = []
        postfix = []
        for token in tokens:
            if (
                token.isdigit()
                or (token[0] == "-" and token[1:].isdigit())
                or "." in token
            ):
                postfix.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and self._get_operator_priority(
                    stack[-1]
                ) >= self._get_operator_priority(token):
                    postfix.append(stack.pop())
                stack.append(token)
        while stack:
            postfix.append(stack.pop())
        return postfix

    def _evaluate_postfix(self, postfix_expr: list) -> float:
        stack = []
        for token in postfix_expr:
            if (
                token.isdigit()
                or (token[0] == "-" and token[1:].isdigit())
                or "." in token
            ):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise Exception("Отсутствует операнд")
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise Exception("Деление на ноль не разрешено")
                    stack.append(a / b)
        if len(stack) != 1:
            raise Exception("Некорректное выражение")
        return stack[0]
