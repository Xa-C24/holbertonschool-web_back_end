#!/usr/bin/env python3
"""Module for pagination."""

import csv
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
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

    def dataset(self) -> List[List]:
        """Loads the dataset from the CSV file."""
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    # Skip the header row
                    self.__dataset = [row for row in reader][1:]
            except FileNotFoundError:
                self.__dataset = []
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        # Validate arguments
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Calculate the start and end indices for the requested page
        start, end = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # If start index is out of range, return an empty list
        if start >= len(dataset):
            return []

        # Return the slice of the dataset corresponding to the requested page
        return dataset[start:end]

# Example usage for testing
if __name__ == "__main__":
    server = Server()

    # Test cases
    try:
        print(server.get_page(1, 3))  # First page, 3 items per page
        print(server.get_page(3, 2))  # Third page, 2 items per page
        print(server.get_page(3000, 100))  # Out-of-range page
    except AssertionError as e:
        print(f"AssertionError: {e}")
