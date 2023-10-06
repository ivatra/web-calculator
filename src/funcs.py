import random
import string


def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


# Мат выражение - *, /, -, +
# Считать количество закрытых и незакрытых скобочек - это хуйня
#
# Создать список приорететных символов типо / *
# Проходится по каждому символу и если встречаются приоритетные символы то мы идем вниз пока не встретим - + и ставим скобку
# Тоесть будет ( если идем назад и ) если идем вперед
# Мы нашли точку остановки ( возвращаемся к предыдущему индексу и затем идем вперед) 
def validate_and_calculate_expression(
    expr: str, err=""
) -> [int, str | None]:  # [str,isValid]
    rando = random.randint(1, 100)
    return [rando, err]
