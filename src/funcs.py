import random
import string

from calculator import Calculator


def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def calculate_expression(expr: str) -> float:
    calculator = Calculator(expr=expr,ndigits=2)
    try:
        result = calculator.calculate()
    except ValueError as e:
        raise ValueError(e) from e

    return result
