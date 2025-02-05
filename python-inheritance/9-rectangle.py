#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

# Importation de la classe BaseGeometry depuis le fichier '7-base_geometry'
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        # Validation des paramètres width et height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
    
    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height
