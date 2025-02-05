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
        """Affichage du rectangle sous la forme [Rectangle] width/height."""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height
