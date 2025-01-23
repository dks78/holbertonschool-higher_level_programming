#!/usr/bin/python3
"""
This module contains the matrix_divided function.

The matrix_divided function takes a matrix and a divisor,
and returns a new matrix with each element divided by the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div and returns a new matrix.
    
    Parameters:
    matrix (list of lists of int/float): The original matrix.
    div (int, float): The divisor.
    
    Returns:
    list of lists of float: A new matrix with the divided values.
    
    Raises:
    TypeError: If the matrix elements are not lists of integers/floats,
               or if div is not an integer/float.
    ZeroDivisionError: If div is zero.
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
