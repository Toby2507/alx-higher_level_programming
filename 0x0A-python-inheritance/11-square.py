#!/usr/bin/python3
"""
Contains a class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square blueprint

    Attributes:
        size (int): square's width

    Methods:
        area: computes the area of the square
    """

    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """returns unofficial string representation"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """computes the area of the square"""
        return self.__size ** 2
