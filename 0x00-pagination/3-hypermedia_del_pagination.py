#!/usr/bin/env python3
"""
This module provides a Server class to paginate a database
of popular baby names
"""

import csv
from typing import List, Dict, Any
import math


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination with index resilence to deletions
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index < total_items, "Index out of range."

        data = []
        current_index = index
        next_index = index

        while len(data) < page_size and next_index < total_items:
            item = indexed_dataset.get(next_index)
            if item is not None:
                data.append(item)
            next_index += 1

        next_index = next_index if next_index < total_items else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
