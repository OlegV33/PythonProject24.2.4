import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 2) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 4) == 1

    def teardown(self):
        print('Выполнение метода Teardown')
