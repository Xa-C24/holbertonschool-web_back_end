#!/usr/bin/env python3
"""A module for creating a tuple from a string and a squared number."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number (integer or float).

    Returns:
        Tuple[str, float]: A tuple where the first element is the string,
        and the second element is the square of the number as a float.
    """

    return (k, float(v ** 2))
