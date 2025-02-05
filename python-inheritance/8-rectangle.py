#!/usr/bin/python3
class BaseGeometry:
    """Représente la géométrie de base."""

    def area(self):
        """Méthode qui doit être implémentée par les classes dérivées."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide si 'value' est un entier et est supérieur à 0.

        Args:
            name (str): Le nom du paramètre à valider.
            value (int): La valeur à valider.

        Lève:
            TypeError: Si 'value' n'est pas un entier.
            ValueError: Si 'value' est inférieur ou égal à 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Représente un rectangle, héritant de BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialise un rectangle avec la largeur et la hauteur spécifiées.
        Valide les entrées en utilisant la méthode 'integer_validator' de BaseGeometry.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Lève:
            TypeError: Si 'width' ou 'height' ne sont pas des entiers.
            ValueError: Si 'width' ou 'height' sont inférieurs ou égaux à 0.
        """
        self.integer_validator("width", width)  # Validation pour la largeur
        self.integer_validator("height", height)  # Validation pour la hauteur
  # Validation pour la hauteur
        self._width = width
        self._height = height

