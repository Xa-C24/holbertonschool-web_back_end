#!/usr/bin/env python3
""" Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """
    List all documents in a collection.
    
    Args:
        mongo_collection: The pymongo collection object.
    
    Returns:
        A list of all documents in the collection, or an empty list if no document.
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
