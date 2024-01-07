#!/usr/bin/python3

"""
This module contains a function to print a list of integers.
"""


def print_list_integer(my_list):
    """
    Prints each integer in the given list.
    Args:
        my_list (list): The list of integers to print.
    """
    for _, num in enumerate(my_list):
        print(f"{num:d}")
