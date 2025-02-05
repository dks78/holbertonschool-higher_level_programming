#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        """Initializes a square object.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        return self.__size * self.__size 
    