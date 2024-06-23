#!/usr/bin/python3
"""  lists states """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id = states.id""")
    city = cur.fetchall()
    for x in city:
        print(x)
    cur.close()
    mydb.close()
