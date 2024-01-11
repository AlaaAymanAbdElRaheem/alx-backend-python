#!/usr/bin/env python3
"""defines a type-annotated function"""

from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
