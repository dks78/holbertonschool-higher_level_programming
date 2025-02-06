#!/usr/bin/env python3
import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre de la forme."""
        pass


class Circle(Shape):

    def __init__(self, radius):

        """Initialisation avec le rayon du cercle."""
        self.radius = radius

    def area(self):
        """Calcul de l'aire du cercle: π * rayon^2."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcul du périmètre du cercle: 2 * π * rayon."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):

        """Initialisation avec la largeur et la hauteur du rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calcul de l'aire du rectangle: largeur * hauteur."""
        return self.width * self.height

    def perimeter(self):
        """Calcul du périmètre du rectangle: 2 * (largeur + hauteur)."""
        return 2 * (self.width + self.height)


def shape_info(shape):

    """Affiche l'aire et le périmètre de la forme passée en argument."""

    print(f"Aire: {shape.area()}")
    print(f"Périmètre: {shape.perimeter()}")
