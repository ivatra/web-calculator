from calculator.math_operators import Addition, Division, Multiplication, Subtraction

# Лучше обьявить это в глобальной области видимости,
# а не в классе, чтобы не иницилизировать этот объект каждый раз как создается экземпляр класса
# Также он находится именно в этом файле, а не в math_operators файле чтобы не нарушать SRP принцип,
# а так же потому как у каждого модуля может быть своя реализация этих классов
math_operators = {
    "+": Addition(),
    "-": Subtraction(),
    "*": Multiplication(),
    "/": Division(),
}


class PostfixEvaluator:
    def __init__(self, postfix_expr: list):
        self.postfix_expr = postfix_expr

    def evaluate(self) -> float:
        stack = []
        for token in self.postfix_expr:
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
                operation = math_operators.get(token)
                if operation:
                    result = operation.execute(a, b)
                    stack.append(result)
                else:
                    raise Exception(f"Неподдерживаемая операция: {token}")

        if len(stack) != 1:
            raise Exception("Некорректное выражение")
        return stack[0]
