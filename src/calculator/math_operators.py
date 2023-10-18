from abc import ABC, abstractmethod


class MathOperation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(MathOperation):
    def execute(self, a, b):
        return a + b

class Subtraction(MathOperation):
    def execute(self, a, b):
        return a - b


class Multiplication(MathOperation):
    def execute(self, a, b):
        return a * b


class Division(MathOperation):
    def execute(self, a, b):
        if b == 0:
            raise Exception("Деление на ноль не разрешено")
        return a / b