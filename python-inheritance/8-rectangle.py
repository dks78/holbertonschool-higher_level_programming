#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

class BaseGeometry:
    
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        
        """
        Validates that `value` is an integer and greater than 0.

        Args:
        name (str): The name of the variable (used in error messages).
        value (any): The value to validate.

        Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than or equal to 0.
        """
         
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
