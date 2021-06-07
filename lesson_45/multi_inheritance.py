class AddCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


class SubCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sub(self):
        return self.a - self.b


class Calculation(AddCalc, SubCalc):

    def __init__(self, a, b):
        AddCalc.__init__(self, a, b)
        SubCalc.__init__(self, a, b)

    def run(self):
        return self.add() + self.sub()

