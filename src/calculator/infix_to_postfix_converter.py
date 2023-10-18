class InfixToPostfixConverter:
    def __init__(self, tokens: list):
        self.tokens = tokens

    def convert(self) -> list:
        stack = []
        postfix = []
        for token in self.tokens:
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

    def _get_operator_priority(self, operator) -> int:
        if operator in ["+", "-"]:
            return 1
        elif operator in ["*", "/"]:
            return 2
        return 0
