#!/usr/bin/python3
"""  writes all cities in database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (argv[4],))
    rows = cur.fetchall()
    re = []
    n = 0
    for row in rows:
        re.append(rows[n][0])
        n += 1
    sep = ", ".join(re)
    print(sep)
    cur.close()
    db.close()
