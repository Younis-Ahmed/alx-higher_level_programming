#!/usr/bin/python3
"""
This module provides a function for returning multiple values.
"""


def multiple_returns(res):
    """
    Return the length of a string and its first character.

    Args:
        res (str): The input string.

    Returns:
        tuple: A tuple containing the length of
          the string and its first character.
    """
    if res == "":
        return (0, None)
    return (len(res), res[0])
