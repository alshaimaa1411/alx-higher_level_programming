#!/usr/bin/python3
"""  lists states """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM ststes WHERE name LIKE %s", (state, ))
    states = cur.fetchall()
    for x in states:
        print(x)
    cur.close()
    mydb.close()
