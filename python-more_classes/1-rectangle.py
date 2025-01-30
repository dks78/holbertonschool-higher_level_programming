#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height properties.
It includes validation to ensure that width and height are non-negative integers.
"""

class Rectangle:
    """A class that defines a rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with given width and height.

        :param width: The width of the rectangle (must be an integer >= 0).
        :param height: The height of the rectangle (must be an integer >= 0).
        """
        self.width = width   # Calls the width setter for validation
        self.height = height # Calls the height setter for validation

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
            raise TypeError("width must be an integer")  # Ensures width is an integer
        if value < 0:
            raise ValueError("width must be >= 0")  # Ensures width is non-negative
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
            raise TypeError("height must be an integer")  # Ensures height is an integer
        if value < 0:
            raise ValueError("height must be >= 0")  # Ensures height is non-negative
        self.__height = value
