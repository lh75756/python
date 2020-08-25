import os
import pytest
import yaml
import allure
from homework.calculator import Calculator

@pytest.mark.run(order=1)
def test_add(Fixture):
    calc = Calculator()
    calc.add(1,2)
@pytest.mark.run(order=3)
def test_sub(Fixture):
    calc = Calculator()
    calc.sub(10,5)
@pytest.mark.run(order=4)
def test_mul(Fixture):
    calc = Calculator()
    calc.mul(20,2)
@pytest.mark.run(order=2)
def test_div(Fixture):
    calc = Calculator()
    calc.div(30,5)






