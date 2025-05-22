import functools


def add(number1, number2):
    return number1 + number2


def get_total(*numbers):
    return functools.reduce(lambda x, y: x + y, numbers)


class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def subtract(self):
        return self.number1 - self.number2