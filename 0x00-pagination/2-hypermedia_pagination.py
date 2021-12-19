#!/usr/bin/env python3
"""
 module to return paginaged data
"""
import csv
import math
from typing import List, Tuple, Union, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''function that returns start index & range of pagination'''
    sind: int = 0
    eind: int = 0

    if page != 1:
        sind = (page - 1) * page_size
    eind = sind + page_size

    return (sind, eind)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns pages specified in page & page_size
        """
        pg: List[List] = []
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indx: Tuple[int, int] = index_range(page, page_size)
        data: List[List] = self.dataset()
        datasize: int = len(data)
        start: int = indx[0]
        for i in range(start, indx[1]):
            if i > datasize:
                return []
            pg.append(data[i])
        return pg

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> dict:
        """Returns summary information
        """
        data: List[List] = self.get_page(page, page_size)
        size: int = len(data)
        next_page: Optional[int] = page + 1 if page + 1 <= size else None
        prev_page: Optional[int] = page - 1 if page - 1 > 0 else None
        return {'page_size': page_size, 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': size}
