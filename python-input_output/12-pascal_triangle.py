#!/usr/bin/python3
"""
Module for task 12 - Pascal triangle
"""

def pascal_triangle(n):
    """
    Printing a pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

    for j in range(len(prev_row) - 1):
        new_row.append(prev_row[j] + prev_row[j + 1])