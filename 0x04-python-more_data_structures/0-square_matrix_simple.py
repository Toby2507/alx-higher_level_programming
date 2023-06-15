#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        n_mat = matrix[:]
        return [list(map(lambda x: x**2, row)) for row in n_mat]
