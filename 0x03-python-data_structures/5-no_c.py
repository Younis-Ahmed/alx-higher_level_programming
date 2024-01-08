#!/usr/bin/python3
"""
This module provides a function to remove all occurrences of the letter 'c'
(case-insensitive) from a string.
"""


def no_c(my_string):
    """
    Remove all occurrences of the letter 'c' (case-insensitive) from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The modified string with 'c' removed.
    """
    res = ''
    for _, char in enumerate(my_string):
        if char.lower() != 'c':
            res += char
    return res
