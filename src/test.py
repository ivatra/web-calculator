def tokenize(expr):
    operators = set(["+", "-", "(", ")"])
    result = []
    i = 0

    def parse_expression():
        nonlocal i
        tokens = []

        while i < len(expr):
            if expr[i] in operators:
                tokens.append(expr[i])
                i += 1
            elif expr[i].isdigit() or (expr[i] == "-" and (i == 0 or expr[i - 1] in operators)):
                if expr[i] == "+" and i > 0 and expr[i - 1] == "+":
                    i += 1  # Убираем плюс перед положительным числом
                start_index = i

                while i < len(expr) and (expr[i].isdigit() or (expr[i] == "-" and i == start_index)):
                    i += 1

                tokens.append(expr[start_index:i])
            elif expr[i] == "(":  # Обрабатываем открывающие скобки
                i += 1
                tokens.append(parse_expression())  # Рекурсивно парсим вложенное выражение
            elif expr[i] == ")":  # Обрабатываем закрывающие скобки
                i += 1
                break
            else:
                raise ValueError("Invalid character in expression")

        return tokens

    result.extend(parse_expression())
    return result

# Пример использования:
expression = "(+10 + +20) + (-100 - 10)"
tokens = tokenize(expression)
print(tokens)
