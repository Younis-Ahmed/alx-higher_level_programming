#!/usr/bin/python3

"""
This module provides a function to delete an element
from a list at a given index.
"""


def delete_at(my_list, idx):
    """
    Delete an element from a list at a given index.

    Args:
        my_list (list): The list to delete from.
        idx (int): The index of the element to delete.

    Returns:
        list: The modified list.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
