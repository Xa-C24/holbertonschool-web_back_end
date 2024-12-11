#!/usr/bin/env python3
""" function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Retourne une liste d'écoles ayant un topic spécifique.
    """
    # Utilisation de la méthode `find` avec un filtre sur le champ 'topics'
    return list(mongo_collection.find({"topics": topic}))
