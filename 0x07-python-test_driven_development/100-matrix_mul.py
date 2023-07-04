#!/usr/bin/python3
"""
module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices

    Args:
        m_a: matrix one
        m_b: matrix two
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any(type(val) not in [int, float] for row in m_a for val in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(val) not in [int, float] for row in m_b for val in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_mat = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_a[0])):
                val += m_a[i][k] * m_b[k][j]
            new_row.append(val)
        new_mat.append(new_row)
    return new_mat
