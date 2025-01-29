#!/usr/bin/python3
"""Module that defines a Square class."""

#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # Utilisation du setter pour initialiser _size
        self.position = position  # Utilisation du setter pour initialiser _position

    @property
    def size(self):
        return self._size  # Retourne la valeur de _size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Vérifie si la valeur est un entier
            raise TypeError("size must be an integer")
        if value < 0:  # Vérifie si la valeur est >= 0
            raise ValueError("size must be >= 0")
        self._size = value  # Assigne la valeur

    @property
    def position(self):
        return self._position  # Retourne la valeur de _position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value  # Assigne la valeur à _position
    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2
    
    def my_print(self):
        """Print the square with the character #."""
        if self._size == 0:
            print()
        else:
            print("\n".join(["#" * self._size for _ in range(self._size)]))
