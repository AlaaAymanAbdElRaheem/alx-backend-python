#!/usr/bin/env python3
"""defines a type-annotated function"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats"""
    return sum(mxd_lst)
