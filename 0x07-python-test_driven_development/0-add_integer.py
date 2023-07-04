#!/usr/bin/python3
"""
add 2 integers module
"""


def add_integer(a, b=98):
    """adds 2 integers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        summ of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b
