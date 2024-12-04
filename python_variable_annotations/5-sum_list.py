#!/usr/bin/env python3
"""A module for summing a list of floats."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all numbers in the list.
    """

    return sum(input_list)
