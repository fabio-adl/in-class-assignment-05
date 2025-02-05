import pytest

from src.my_funcs import get_largest_value_in_list

def test_get_largest_value_in_list_1():
    res = get_largest_value_in_list([])
    assert res == None

def test_get_largest_value_in_list_2():
    res = get_largest_value_in_list([1,2,3])
    assert res == 3

def test_get_largest_value_in_list_3():
    res = get_largest_value_in_list([3,2,1])
    assert res == 3

def test_get_largest_value_in_list_4():
    res = get_largest_value_in_list([3,3,3])
    assert res == 3