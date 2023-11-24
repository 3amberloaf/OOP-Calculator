"""Calculator class and +,/,-,* classes"""

from app.operations import *

#Calculator class
class Calculation:
    """Abstract base Calculator class"""

    #Factory Method
    @classmethod
    def create(cls, val1, val2):
        return cls (val1, val2)
    #Constructor
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    #Setting and Getting the results/variables
    def set_result(self, result):
        self.result = result

    def set_val1(self, val1):
        self.val1 = val1
    def set_val2(self, val2):
        self.val2 = val2

    def get_result(self):
        pass

    def get_val1(self):
        return self.val1

    def get_val2(self):
        return self.val2
    def __repr__(self):
      return f'Operation: {type(self)}, (val1={self.val1}, val2={self.val2}, result={self.get_result()})'

class Addition(Calculation):
    def get_result(self):
        return addition(self.val1, self.val2)

class Subtraction(Calculation):
    def get_result(self):
        return subtraction(self.val1, self.val2)

class Multiplication(Calculation):
    def get_result(self):
        return multiplication(self.val1, self.val2)

class Division(Calculation):
    def get_result(self):
        return division(self.val1, self.val2)