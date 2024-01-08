#!/usr/bin/python3

"""
This module contains a function to find the maximum integer in a list.
"""


def max_integer(my_list):
    """
    Find the maximum integer in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The maximum integer in the list.
    """
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for _, num in enumerate(my_list):
        if num > big:
            big = num
    return big
