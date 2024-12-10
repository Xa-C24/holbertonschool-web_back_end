#!/usr/bin/env python3
""" Module for deletion-resilient hypermedia pagination."""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: A dictionary where keys are indices, and values are rows of the dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def dataset(self) -> List[List]:
        """Loads the dataset from the CSV file."""
        if self.__dataset is None:
          with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            # Ignore the header row
            self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Provides a deletion-resilient pagination response.

        Args:
            index (int): The start index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata and the page data.
        """
        # 1. Validation des arguments
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), \
            "Index must be a valid integer within dataset range."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        # 2. Obtenir le dataset indexé
        indexed_data = self.indexed_dataset()

        # 3. Collecter les données pour la page et calculer le prochain index
        data = []
        current_index = index  # Initialisation de current_index

        for _ in range(page_size):
            # Ignorer les indices supprimés
            while current_index not in indexed_data and current_index < len(indexed_data):
                current_index += 1
            # Si on atteint la fin des données disponibles
            if current_index >= len(indexed_data):
                break
            # Ajouter la donnée et passer au suivant
            data.append(indexed_data[current_index])
            current_index += 1

        # 4. Construire et retourner le dictionnaire de résultat
        next_index = current_index if current_index < len(indexed_data) else None
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
