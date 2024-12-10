#!/usr/bin/env python3
"""Module for pagination."""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for a page of data.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server instance."""
        self.__dataset = None

    def dataset(self) -> List[list]:
        """Loads the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Skip the header row
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Calculate the start and end indices for the requested page
        start, end = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # If start index is out of range, return an empty list
        if start >= len(dataset):
            return []

        # Return the slice of the dataset corresponding to the requested page
        return dataset[start:end]
