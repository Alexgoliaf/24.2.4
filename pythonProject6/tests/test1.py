import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator
    def test_multiply_try(self):
        assert self.calc.multiply(self,3,4)==12
    def test_division_try(self):
        assert self.calc.division(self,15,5)==3
    def test_subtraction_try(self):
        assert self.calc.subtraction(self,20,7)==13
    def test_adding_try(self):
        assert self.calc.adding(self,5,6)==11
        