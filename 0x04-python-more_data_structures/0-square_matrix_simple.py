#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        n_mat = matrix[:]
        return [[row[i] ** 2 for i in range(len(n_mat))] for row in n_mat]
