import pytest
def soma(a, b):
    return a + b

def test_1():
    assert soma(1, 2) == 3

def test_2():
    assert soma(2, 2) == 4

def test_3():
    assert soma(0, 0) == 0

def test_4():
    assert soma(-1, -1) == -2

def test_5():
    assert soma(-1, 1) == 0