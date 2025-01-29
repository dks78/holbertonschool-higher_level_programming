#!/usr/bin/python3
class Square:
    """Classe qui définit un carré avec un attribut privé size."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille optionnelle."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # On affecte size seulement après validation

    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille du carré avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2
