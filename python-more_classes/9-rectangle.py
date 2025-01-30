#!/usr/bin/python3

"""
This module defines a Rectangle class with width and height properties.
It includes validation to ensure that width and height
are integers and greater than or equal to 0.
"""
class Rectangle:
    # Attributs de classe
    number_of_instances = 0  # Initialisé à 0
    print_symbol = "#"  # Utilisé comme symbole pour la représentation du rectangle
    
    def __init__(self, width=0, height=0):
        """
        Initialise une instance de Rectangle avec une largeur et une hauteur spécifiées.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrémente le nombre d'instances à chaque création
    
    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Valide et définit la largeur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retourne la hauteur du rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Valide et définit la hauteur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Retourne le périmètre du rectangle. Si la largeur ou la hauteur est 0, retourne 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Retourne la représentation en chaîne de caractères du rectangle avec le symbole #."""
        if self.width == 0 or self.height == 0:
            return ""  # Si la largeur ou la hauteur est 0, retourner une chaîne vide
        return (str(self.print_symbol) * self.width + "\n") * self.height
    
    def __repr__(self):
        """Retourne une chaîne de caractères qui permet de recréer l'objet avec eval()"""
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """Affiche un message lors de la suppression d'une instance de Rectangle."""
        Rectangle.number_of_instances -= 1  # Décrémente le nombre d'instances
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Méthode statique qui retourne le rectangle ayant la plus grande surface.
        Si les deux rectangles ont la même surface, retourne rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        """Retourne une instance de Rectangle avec une largeur et une hauteur égales à size."""
        return cls(size, size)
