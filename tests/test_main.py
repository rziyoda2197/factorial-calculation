import pytest
from math import factorial

def optimised_factorial(n):
    if n == 0:
        return 1
    else:
        return n * optimised_factorial(n-1)

def test_optimised_factorial():
    assert optimised_factorial(0) == 1
    assert optimised_factorial(1) == 1
    assert optimised_factorial(2) == 2
    assert optimised_factorial(3) == 6
    assert optimised_factorial(4) == 24
    assert optimised_factorial(5) == 120

def test_optimised_factorial_large_input():
    assert optimised_factorial(10) == factorial(10)
    assert optimised_factorial(15) == factorial(15)
    assert optimised_factorial(20) == factorial(20)

def test_optimised_factorial_invalid_input():
    with pytest.raises(TypeError):
        optimised_factorial(-1)
    with pytest.raises(TypeError):
        optimised_factorial(1.5)
    with pytest.raises(TypeError):
        optimised_factorial("10")
