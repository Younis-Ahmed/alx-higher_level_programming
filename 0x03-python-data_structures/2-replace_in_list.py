#!/usr/bin/python3

"""
This module provides a function to replace
an element in a list at a given index.
"""


def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a given index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element (any): The new element to replace the existing one.

    Returns:
        list: The modified list.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list
