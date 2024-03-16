#!/usr/bin/python3
""" list all databases """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    safe_match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (safe_match, ))
    rows_number = cursor.fetchall()
    for n in rows_number:
        print(n)
    cursor.close()
    db.close()
