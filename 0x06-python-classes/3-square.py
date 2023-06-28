#!/usr/bin/python3
"""
This module contains a class named Square that defines a square.
It is based on file 2-square.py
"""


class Square:
    """A class representing a square.

    Methods:
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
