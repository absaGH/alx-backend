#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Improved pagination
        """
        lindex: int = len(self.__indexed_dataset) - 1
        indx: int = 0 if index is None else index
        assert indx <= lindex
        next_index: int = 0
        data: List[List] = []
        while indx not in self.__indexed_dataset:
            indx = (indx + page_size) - 1
        for i in range(indx, (indx + page_size)):
            data.append(self.__indexed_dataset[i])
        next_index = i + 1
        return {'index': indx, 'data': data,
                'page_size': page_size, 'next_index': next_index}
