#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a square.
        
        Args:
            size (int): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
