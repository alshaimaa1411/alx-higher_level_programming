#!/usr/bin/python3
"""  lists states """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("""SELECT * FROM states WHERE name 
                LIKE BINARY 'N%' ORDER BY state.id""")
    names = cur.fetchall()
    for name in names:
        print(name)
    cur.close()
    mydb.close()
