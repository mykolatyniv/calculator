from CsvReader import CsvReader

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = a / b
    return c

def square(a):
    a = int(a)
    c = a**2
    return c

def square_root(a):
    a = int(a)
    c = a**.5
    return c

def mean(data):
    mean = data
    return mean

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

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result

    class CSVStats(Calculator):
        data = []

        def __init__(self, data_file):
            self.data = CsvReader(data_file)
            pass

        def mean(self):
            mean(self.data)