#!/usr/bin/python3
"""
module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix: matrix to be divided
        div: divisor

    Returns:
        new matrix (success), raises Exception otherwise
    """
    errMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or matrix == []:
        raise TypeError(errMsg)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(errMsg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for col in row:
            if type(col) in [int, float]:
                new_row.append(round(col / div, 2))
            else:
                raise TypeError(errMsg)
        new_matrix.append(new_row)
    return new_matrix
