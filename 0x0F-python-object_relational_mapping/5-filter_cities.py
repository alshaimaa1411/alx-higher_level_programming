#!/usr/bin/python3
"""" cities names"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", usernsme=sys.argv[1], password=sys.argv[2],
                           dbname=sys.argv[3], port=3306)
    cur = mydb.cursor()
    state = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities
                WHERE INNER JOIN states
                cities.state_id = states.id""")
    city = cur.fetchall()
    for x in city:
        print(x)
    cur.close()
    mydb.close()
