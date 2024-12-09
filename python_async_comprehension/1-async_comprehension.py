#!/usr/bin/env python3
""" """

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers asynchronously.

    This function:
    - Iterates over the async_generator using an async comprehension.
    - Collects the 10 random numbers into a list.
    - Returns the list.

    Returns:
        List of 10 random floating-point numbers.
    """
    # Utiliser une compréhension asynchrone pour collecter tous les nombres
    return [value async for value in async_generator()]
