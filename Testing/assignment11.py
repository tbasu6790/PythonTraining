'''
Test the conditions for factorial, prime number, area of circle 
with passign wrong paramters as 0. 
Make sure you try to test using both the unittest and pytest 
Example testcases below: 
(a) factorial by passing 4 and 0 
(b) prime number by passing 31, 17, 0 
(c) area of circle by passing 4, 0
'''

import math

def factorial(n: int) -> int:
    """Return factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def area_of_circle(radius: float) -> float:
    """Return area of circle given radius."""
    if radius <= 0:
        raise ValueError("Radius must be greater than 0")
    return math.pi * radius * radius
