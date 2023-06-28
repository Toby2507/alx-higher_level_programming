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
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """:obj:`tuple` of `int`: position to start printing from

        Has to be a tuple of positive numbers
        """
        return self.__position

    @position.setter
    def position(self, pos):
        a, b = pos
        err = "position must be a tuple of 2 positive integers"
        if isinstance(pos, tuple) and len(pos) == 2 and a >= 0 and b >= 0:
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError(err)
            self.__position = pos
        else:
            raise TypeError(err)

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the circle
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square in character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.position[-1]):
            print()
        for _ in range(self.size):
            print(" " *self.position[0], end="")
            print("#" * self.size)
