import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply

def test_multiply():
    res = multiply(10,2)
    assert res == 20

# Check for understanding
## Test difference

def test_difference():
    res = difference(5,-2)
    assert res == 7

# Work together
## Test absolute sum

def test_absolute_sum():
    res = absolute_sum(-1,1)
    assert res == 2

def test_absolute_sum_2():
    res = absolute_sum(1,1)
    assert res == 2

# Check for understanding
## Test calculate age

def test_calculate_birth_year():
    res = calculate_birth_year(2025, 43, False)
    assert res == 1981

def test_calculate_birth_year_1():
    res = calculate_birth_year(2025, 44, True)
    assert res == 1981