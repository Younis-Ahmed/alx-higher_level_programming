#!/usr/bin/python3
"""
This module contains a function to print a list of integers in reverse order.
"""


def print_reversed_list_integer(my_list):
    """
    Prints a list of integers in reverse order.

    Args:
        my_list (list): The list of integers.

    Returns:
        None
    """
    my_list.reverse()
    for i, num in enumerate(my_list):
        print(f'{num:d}')
