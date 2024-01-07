#!/usr/bin/python3
"""
This module provides a function to retrieve an element
from a list at a given index.
"""


def element_at(my_list, idx):
    """
    Retrieve the element at the given index in the list.

    Args:
        my_list (list): The list to retrieve the element from.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the given index, or None if the index is out of range.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
