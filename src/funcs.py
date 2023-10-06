import random
import string
from re import search

def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str

def __is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calculate_expression(expr: str, math_signs = ["(", ")", "+", "-", "/", "*", " "]) -> float:
    # Проверка на пустое выражение или пустые скобки
    if not expr.strip() or search(r'\(\s*\)', expr):
        raise ValueError("Выражение пустое или имеет пустые скобки ")
    # Проверка на одинаковое количество скобок
    if expr.count('(') != expr.count(')'):
        raise ValueError("Несбалансированные круглые скобки")

    try:
        result = eval(expr)
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Нельзя делить на ноль') from e
    except Exception as e:
        raise ValueError("Не валидное выражение") from e

    return float("{:.2f}".format(result)) if isinstance(result, float) else float(result)

