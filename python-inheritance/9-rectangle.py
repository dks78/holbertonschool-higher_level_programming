#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

# Importing the BaseGeometry class from the '7-base_geometry' file
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate the width and height parameters
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
           
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
 