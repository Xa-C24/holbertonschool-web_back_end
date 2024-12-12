#!/usr/bin/env python3
"""
Python script that provides some stats
about Nginx logs stored in MongoDB.
"""

import subprocess
import json

def log_stats():
    """
    Affiche des statistiques sur les logs Nginx
    dans la base de données MongoDB en utilisant la CLI.
    """
    # Nombre total de logs
    total_logs = subprocess.check_output(
        ['mongo', 'logs', '--quiet', '--eval',
         'db.nginx.countDocuments({})']
    ).strip().decode('utf-8')
    print(f"{total_logs} logs")

    # Statistiques des méthodes
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = subprocess.check_output(
            ['mongo', 'logs', '--quiet', '--eval',
             f'db.nginx.countDocuments({{"method": "{method}"}})']
        ).strip().decode('utf-8')
        print(f"\tmethod {method}: {count}")

    # Nombre de requêtes GET avec path /status
    status_check = subprocess.check_output(
        ['mongo', 'logs', '--quiet', '--eval',
         'db.nginx.countDocuments({"method": "GET", "path": "/status"})']
    ).strip().decode('utf-8')
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
