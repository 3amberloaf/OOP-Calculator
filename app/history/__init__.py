"""History class that extends list"""
from app.calculations import Calculation
class History(list):
    def __init__(self, *argv):
        super().__init__(argv)
    def get_last_result(self):
        return self[-1].get_result()
    def print_history(self):
        for calculation in self:
            print(calculation)