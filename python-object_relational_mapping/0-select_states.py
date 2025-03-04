#!/usr/bin/python3
"""
Task 0. Get all states
"""


import MySQLdb
import sys #to allow access to args

if __name__ == "__main__":
    # args check
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host="localhost", #local
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        cursor = db.cursor() #needed to exct sql query
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

        for state in cursor.fetchall(): # loop to check all lines from what query gets
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as err: # in case access is nok
        print(f"Erreur MySQL : {err}")
        sys.exit(1)

# Note to self : user created, molly
# test line : python3 0-select_states.py molly molly_pwd hbtn_0e_0_usa
