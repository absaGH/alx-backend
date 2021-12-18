#!/usr/bin/env python3
from typing import Tuple
'''module to find index of pagination'''


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''function that returns start index & range of pagination'''
    sind: int = 0
    eind: int = 0

    if page != 1:
        sind = (page - 1) * page_size
    eind = sind + page_size

    return (sind, eind)
