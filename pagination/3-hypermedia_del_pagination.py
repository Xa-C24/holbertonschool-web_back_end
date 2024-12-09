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
                self.__dataset = [row for row in reader][1:]  # Ignore the header row
        return self.__dataset


    def get_hyper_index(self, index=None, page_size: int = 0) -> Dict:
        """
        Provides a deletion-resilient pagination response.

        Args:
            index (int): The start index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata and the page data. 
        """
        # 1. Valider que l'index est dans la plage correcte
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        # 2. Obtenir le dataset indexé
        indexed_data = self.indexed_dataset()

        # 3. Initialiser les données de la page et calculer le prochain index
        data = []
        next_index = index

        for _ in range(page_size):
            # Ignorer les indices supprimés
            while next_index not in indexed_data and next_index < len(indexed_data):
              next_index += 1
            # Si on atteint la fin des données disponibles
            if next_index >= len(indexed_data):
                break
            # Ajouter la donnée à la page et incrémenter l'indice
            data.append(indexed_data[next_index])
            next_index += 1

        # 4. Construire et retourner le dictionnaire de résultat
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
