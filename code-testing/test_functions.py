import pytest
import functions as funcs

#add testing
def test_add():
    assert 5 == funcs.add(2,3)

#div testing
def test_div():
    assert 2 == funcs.add(20,10)

def test_div_by_0():
    assert 5 == funcs.add(2,3)