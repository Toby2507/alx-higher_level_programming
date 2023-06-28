#!/usr/bin/python3
"""
This module contains a class called Square that defines a square.
It is based on file 4-square.py
"""


class Square:
    """A class representing a square.

    Methods:
        area(self): Calculates and returns the area of the square
        my_print(self): Prints the square in character #
    """
    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size

    @property
    def size(self):
        """int: Size of the square

        Size has to be a positive integer
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square in character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
