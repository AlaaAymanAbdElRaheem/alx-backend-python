#!/usr/bin/env python3
"""defining a type-annotated function"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
