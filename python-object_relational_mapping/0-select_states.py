#!/usr/bin/python3
"""
Task 0. Get all states
"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> \
            <mysql_password> <database_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

        for state in cursor.fetchall():
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as err:
        print(f"Erreur MySQL : {err}")
        sys.exit(1)
