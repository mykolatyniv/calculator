def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    return c

def square(a):
    a = int(a)
    c = a ** 2
    return c

def square_root(a):
    a = int(a)
    c = a**.5
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def squaring(self, a):
        self.result = square(a)
        return self.result

    def square_rooting(self, a):
        self.result = square_root(a)
        return self.result