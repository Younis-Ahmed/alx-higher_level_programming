#!/usr/bin/python3
"""
This module provides a function to print a matrix of integers.
"""


def print_matrix_integer(matrix):
    """
    Prints a matrix of integers.

    Args:
        matrix (list): The matrix to be printed.
    """
    for _, row in enumerate(matrix):
        for j, value in enumerate(row):
            if j != 0:
                print(" ", end='')
            print(f"{value}", end='')
        print('')
