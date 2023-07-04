#!/usr/bin/python3
"""
module contains a function that multiplies 2 matricess by using NumPy
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of 2 matrices using numpy"""
    res = matmul(m_a, m_b)
    return res
