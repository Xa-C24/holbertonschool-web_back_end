#!/usr/bin/env python3
"""A module for calculating the floor of a float."""

import math

def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
