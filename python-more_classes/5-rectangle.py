#!/usr/bin/python3

"""
This module defines a Rectangle class with width and height properties.
It includes validation to ensure that width and height
are integers and greater than or equal to 0.
"""


class Rectangle:
    """A class that defines a rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with given width and height.

        :param width: The width of the rectangle (must be an integer >= 0).
        :param height: The height of the rectangle (must be an integer >= 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the rectangle's width.

        :return: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width with validation.

        :param value: The new width value.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the rectangle's height.

        :return: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height with validation.

        :param value: The new height value.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        :return: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        :return: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        String representation of the rectangle using "#" characters.

        :return: A string that visualizes the rectangle,
        """
        if self.width == 0 or self.height == 0:
            return ""  # If width or height is 0, return an empty string.

        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"

        return rectangle_str.strip()

    def __repr__(self):
        
        """
        Return a string that can be used to recreate the rectangle object.

        :return: A string representation of the Rectangle
        """
        return f"Rectangle({self.width}, {self.height})"
    def __del__(self):
        print("Bye rectangle...")
