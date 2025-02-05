#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initializes a rectangle with width and height."""

        self.integer_validator("height", height)
        self.__width = width  # Private attribute
        self.integer_validator("width", width)
        self.__height = height  # Private attribute
        