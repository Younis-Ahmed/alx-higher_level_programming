#!/usr/bin/python3
"""
This module provides a function to create a new list with an
element replaced at a given index.
"""


def new_in_list(my_list, idx, element):
    """
    Create a new list with an element replaced at a given index.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new element to insert.

    Returns:
        list: The new list with the element replaced.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    res = list(my_list)
    res[idx] = element
    return res
