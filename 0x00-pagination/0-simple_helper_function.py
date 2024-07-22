#!/usr/bin/env python3
"""
This module provides a function to calculate the start and end index
for pagination based on page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number.
        page_size (int): The page size.

    Returns:
        Tuple[int, int]: The start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
