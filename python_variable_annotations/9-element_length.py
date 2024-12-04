#!/usr/bin/env python3
"""A module for calculating the lengths of sequences in an iterable."""


from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each sequence in an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its corresponding length.
    """

    return [(i, len(i)) for i in lst]
