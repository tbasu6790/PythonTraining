import pytest
from assignment11 import factorial, is_prime, area_of_circle

def test_factorial():
    assert factorial(4) == 24
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-5)

def test_is_prime():
    assert is_prime(31) is True
    assert is_prime(17) is True
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-3) is False

def test_area_of_circle():
    assert round(area_of_circle(4), 5) == 50.26548
    with pytest.raises(ValueError):
        area_of_circle(0)
    with pytest.raises(ValueError):
        area_of_circle(-2)
