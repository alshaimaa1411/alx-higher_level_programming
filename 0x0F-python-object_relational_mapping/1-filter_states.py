#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    msql = "SELECT name FROM states WHERE name LIKE 'N%"
    cur.execute(msql)
    names = cur.fetchall()
    for name in names:
        print(name)
    cur.close()
    mydb.close()
