#!/usr/bin/env python3
""" function that inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs to insert as a new document.

    Returns:
        The _id of the inserted document.
    """
    if not mongo_collection:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.insertion_id
