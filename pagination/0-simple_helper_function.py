#!/usr/bin/env python3
""" Write a function named index_range that takes two integer arguments. """


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
