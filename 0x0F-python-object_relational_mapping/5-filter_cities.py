#!/usr/bin/python3
"""" cities names"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    state = sys.argv[4]
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN
                states ON cities.state_id = states.id
                WHERE states.name=%s""", (state, ))
    city = cur.fetchall()
    result = list(row[0] for row in city)
    print(*result, sep=", ")
    cur.close()
    mydb.close()
