#!/usr/bin/python3
"""
This module contains a function to check if elements in a list
are divisible by 2.
"""


def divisible_by_2(my_list):
    """
    Check if elements in a list are divisible by 2.

    Args:
        my_list (list): The list to check.

    Returns:
        list: A list of booleans indicating if each element is divisible by 2.
    """
    mul = []
    for _, num in enumerate(my_list):
        if num % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)

    return mul
