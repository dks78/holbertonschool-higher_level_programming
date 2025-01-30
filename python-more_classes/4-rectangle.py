#!/usr/bin/python3

"""
This module defines a Rectangle class with width and height properties.
It includes validation to ensure that width ands.
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

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

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

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"

        return rectangle_str.strip()
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        new_rectangle = eval(repr(my_rectangle))

