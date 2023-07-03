#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle Class

    Methods:
        area(self): Returns the rectangles's area
        perimeter(self): Returns the rectangle's perimeter
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: width of the rectangle

        width has to be a positive integer
        """
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """int: height of the rectangle

        height has to be a positive integer
        """
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """Calculates the area of the square

        Returns:
            int: rectangle's area
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the square

        Returns:
            int: rectangle's perimeter
        """
        return (2 * self.width) + (2 * self.height)
