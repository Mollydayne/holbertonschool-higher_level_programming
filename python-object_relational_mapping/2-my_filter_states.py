#!/usr/bin/python3
"""
Task 2. Filter states by user input
"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-filter_states.py <mysql_username> <mysql_password> \
            <database_name> <state_name>")
        sys.exit(1)

    try:
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            password=mysql_password,
            database=database_name,
            charset="utf8mb4"
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()
        if not results:
            print("No Sates matching ur request!")
        else:
            for row in results:
                print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as err:
        print(f"Erreur MySQL : {err}")
        sys.exit(1)
