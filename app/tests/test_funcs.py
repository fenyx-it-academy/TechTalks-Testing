import pytest
from app.funcs import inc, subt, prime_number, reverse_word


def test_calc():
    assert inc(1) == 2
    assert subt(1) == 0
    assert subt(0) == -1


def test_reverse_word():
    assert reverse_word('hello') == 'olleh'


def test_prime():
    assert prime_number(4) == '4 is not a prime number'
    assert prime_number(1) == '1 is not a prime number'