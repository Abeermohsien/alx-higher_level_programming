#!/usr/bin/python3
""" list all databases """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4],))
    rows_number = cursor.fetchall()
    i = list(n[0] for n in rows_number)
    print(*i, separator=", ")
    cursor.close()
    db.close()
