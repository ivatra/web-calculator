import random
import string

from sympy import sympify


def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str

def calculate_expression(expr: str) -> float:
    def is_math_operation(expr: str) -> bool:
        operators = set("+-*/")
        return any(op in expr for op in operators)

    if not is_math_operation(expr):
        raise ValueError("Выражение не содержит математических операций")

    if not expr.strip():  # Проверка на пустое выражение
        raise ValueError("Выражение не может быть пустым")

    try:
        result = sympify(expr)
    except Exception as e:
        raise ValueError("Не валидное выражение") from e

    return round(float(result), 2)
