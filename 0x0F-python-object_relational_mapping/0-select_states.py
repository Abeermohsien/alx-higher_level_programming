#!/usr/bin/python3
"""  make a list of all states in database"""
import MySQLdb 
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows_number = cursor.fetchall()
    for r in rows_number:
        print(r)
    cursor.close()
    db.close()
