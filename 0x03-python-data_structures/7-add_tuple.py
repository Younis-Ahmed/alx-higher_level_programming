#!/usr/bin/python3
"""
This module provides a function to add tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise and returns the result.

    Args:
        tuple_a: The first tuple.
        tuple_b: The second tuple.

    Returns:
        A tuple containing the sum of corresponding elements
          from tuple_a and tuple_b.
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
