#!/usr/bin/python3
""" list all the databases """
import MySQLdb
import sys


if __name__ == "__main__":
    db_name = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db_name=sys.argv[3], port=3306)
    cursor = db_name.cursor()
    cursor.execute("SELECT * FROM states")
    n_rows = cursor.fetchall()
    for n in n_rows:
        print(n)
    cur.close()
    db_name.close()
