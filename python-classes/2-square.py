#!/usr/bin/python3
class Square:
    """
    Classe qui définit un carré.

    Attribut d'instance :
        __size (int) : Taille du côté du carré (par défaut 0).
    """
    def __init__(self, size=0):
        """
        Initialise un carré avec une taille optionnelle.

        Args:
            size (int, optionnel) : Taille du côté du carré (par défaut 0).
        
        Raises:
            TypeError : Si size n'est pas un entier.
            ValueError : Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
