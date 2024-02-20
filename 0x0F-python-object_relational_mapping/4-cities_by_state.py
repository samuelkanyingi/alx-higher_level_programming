#!/usr/bin/python3
"""Script to list all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
