#!/usr/bin/python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
