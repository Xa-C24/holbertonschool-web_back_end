#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
    """
    Affiche des statistiques sur les logs Nginx dans la base de données MongoDB.
    """
    # Connexion à MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Nombre total de logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Statistiques des méthodes
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Nombre de requêtes GET avec path /status
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()