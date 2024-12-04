#!/usr/bin/python3
"""a script for type-annotated function add that
takes a float a and a float b as arguments
and returns their sum as a float."""

def add(a: float, b: float) -> float:
    """
    Calculate the sum of two floating-point numbers.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b
