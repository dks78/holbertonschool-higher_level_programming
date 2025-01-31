#!/usr/bin/python3

"""
This module defines a Rectangle class with width and height properties.
It includes validation to ensure that width and height
are integers and greater than or equal to 0.
"""

class Rectangle:
    # Class attributes
    number_of_instances = 0  # Initialized to 0
    print_symbol = "#"  # Used as the symbol for rectangle representation
    
    def __init__(self, width=0, height=0):
        """
        Initializes an instance of Rectangle with specified width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances on each creation
    
    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Validates and sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Validates and sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Returns the perimeter of the rectangle. If width or height is 0, returns 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """Displays a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
    
    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))
