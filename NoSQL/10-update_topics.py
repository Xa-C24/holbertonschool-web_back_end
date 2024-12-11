#!/usr/bin/env python3
""" function that changes all topics of a school document """


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (list): The list of topics to set for the school.
    """
    mongo_collection.update_many(
        {"name": name},  # Filter documents with the specified name
        {"$set": {"topics": topics}}  # Update the "topics" field
    )