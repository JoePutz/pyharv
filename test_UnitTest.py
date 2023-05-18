#This will be used to test UnitTest.py

from UnitTest import square, hello

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
#The above is an accurate test. However, it doesn't scale well, as there will be more things to test
#So we use the "assert" word to do tests differently

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squares was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squares was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
#Better, more concise individually but expanded over more examples is still too much.
#So we use pytest a third party library

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
#pip install pytest
#pytest test_UnitTest.py in terminal

#we can also break things up. Pytest stops after the firt error discovered per each function. So make more functions like so:

def test_postive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
#Doing it this way gave more information. As it shows where it goes wrong with each of the above functions

import pytest

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_helloarg():
    assert hello("David") == "hello, David"

def test_hellomany():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
#You can do this. above works. But you don't want too complicated tests. Tests should be simple so we don't have to test our tests


def test_hellodefault():
    assert hello() == "hello, world"

if __name__ == "__main__":
    main()