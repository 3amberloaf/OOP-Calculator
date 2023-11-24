"""Calculator class"""
from app.calculations import *
from app.history import History

class Calculator:

    #Static history property
    history = History()

    @classmethod
    def add(cls, val1, val2):
        cls.history.append(Addition.create(val1, val2))
        return cls.history.get_last_result()
    @staticmethod

    def subtract(val1, val2):
        return Subtraction.create(val1, val2).get_result()
    def multiply(val1, val2):
        return Multiplication.create(val1, val2).get_result()
    def divide(val1, val2):
        return Division.create(val1, val2).get_result()