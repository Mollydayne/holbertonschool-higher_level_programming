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

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            password=mysql_password,
            database=database_name,
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name\
            = '{}' ORDER BY id ASC;".format(state_name)
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as err:
        print(f"Erreur MySQL : {err}")
        sys.exit(1)
