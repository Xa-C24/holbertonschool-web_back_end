#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def log_stats():
    """
    Affiche des statistiques sur les logs Nginx
    dans la base de données MongoDB en utilisant la CLI.
    """
    # Nombre total de logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Statistiques des méthodes
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Nombre de requêtes GET avec path /status
    # Status check (method=GET and path=/status)
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
