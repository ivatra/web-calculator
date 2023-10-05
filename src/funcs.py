import random
import string


def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def client_validation(expr: str) -> str | None:
    pass


# Мат выражение - *, :, ^, -, +
def validate_and_calculate_expression(
    expr: str, err=""
) -> [int, str | None]:  # [str,isValid]
    rando = random.randint(1, 100)
    return [rando, err]
