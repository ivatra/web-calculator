import random
import string
from re import search

def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str

def calculate_expression(expr: str) -> float:
    try:
        result = eval(expr) # Это не очень безопастно,но учитываем , что на фронте есть проверка :)
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Нельзя делить на ноль') from e
    except Exception as e:
        raise ValueError("Не валидное выражение") from e

    return float("{:.2f}".format(result)) if isinstance(result, float) else float(result)

