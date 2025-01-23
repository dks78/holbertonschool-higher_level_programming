#!/usr/bin/python3
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
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix