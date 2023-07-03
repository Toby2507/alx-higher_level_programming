#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle Class

    Attributes:
        number_of_instances (int): no of instances created
        print_symbol (str): print symbol for __str__

    Methods:
        area(self): Returns the rectangles's area
        perimeter(self): Returns the rectangle's perimeter
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints the rectangle with a print symbol"""
        if not self.width or not self.height:
            return ""
        rectangle = ""
        for _ in range(self.height):
            rectangle += str(self.print_symbol) * self.width + '\n'
        return rectangle.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Performs instance cleanup on instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        if not self.width or not self.height:
            return 0
        return (2 * (self.width + self.height))
