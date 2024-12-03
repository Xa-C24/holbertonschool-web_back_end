#!/usr/bin/python3
from typing import Sequence, Tuple, List, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of a tuple containing a sequence"""
    return [(i, len(i)) for i in lst]
