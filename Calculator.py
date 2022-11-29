class mathOperations:
    def addition(self, a, b):
        self.a = a
        self.b = b
        return a + b

    def subtraction(self, a, b):
        self.a = a
        self.b = b
        return a - b

    def multiplication(self, a, b):
        self.a = a
        self.b = b
        return a * b

    def division(self, a, b):
        self.a = a
        self.b = b
        if b != 0:
            return a / b
        else:
            return "DivisionByZeroError"
