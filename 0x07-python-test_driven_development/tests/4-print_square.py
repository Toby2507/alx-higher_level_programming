#!/usr/bin/python3
"""
module contains a function that prints a square with the character #
"""


def print_square(size):
    """prints a square of specified size

    Args:
        size: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for _ in range(size):
        print('#' * size)
