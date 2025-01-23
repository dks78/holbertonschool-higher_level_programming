#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).
    
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number, defaults to 98.
    
    Returns:
        int: The sum of the two integers.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert to integers before addition
    a = int(a)
    b = int(b)

    return a + b



if __name__ == "__main__":
    import doctest
    doctest.testmod()
