#!/usr/bin/env python3
"""A module for creating a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply a given float by the multiplier.

        Args:
            value (float): The float to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier
    return multiplier_function
