#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Square(BaseGeometry):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    
    def area(self):
        """Calcul l'aire du carré"""
        return self.__size ** 2
    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"