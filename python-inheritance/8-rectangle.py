#!/usr/bin/python3
"""
Module BaseGeometry
====================

This module defines a class `
BaseGeometry` with a method `area()`.

Classes:
--------
- BaseGeometry: A base class
for geometric operations.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initializes a rectangle with width and height."""

        self.integer_validator("height", height)
        self.__width = width 
        self.integer_validator("height", height)# Private attribute
        self.__height = height  # Private attribute
        