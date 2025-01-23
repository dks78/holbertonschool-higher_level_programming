#!/usr/bin/python3
"""
Module for add_integer function
"""


def add_integer(a, b=98):

    """
    Adds two integers.
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number, default is 98.
    Returns:
    int: The sum of a and b, casted to integer.
    Raises:
    TypeError: If a or b are not integers or floats.
    ValueError: If a or b are NaN.
    OverflowError: If a or b are too large to be converted to integers.
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
