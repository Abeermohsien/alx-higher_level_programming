#!/usr/bin/python3
""" list all the states in the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
               user=sys.argv[1], passwd=sys.argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states")
    n_rows = cursor.fetchall()
    for n in n_rows:
        print(n)
    cursor.close()
    database.close()
