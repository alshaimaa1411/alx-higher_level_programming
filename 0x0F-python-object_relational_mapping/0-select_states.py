#!/usr/bin/python3

import MySQLdb
import sys

mydb = MySQLdb.connect(host="localhost", username=sys.argv[1], 
                       password=sys.argv[2], database=sys.argv[3], port=3306)
cur = mydb.cursor()
cur.execute("SELECT * FROM states")
states = cur.fetchall()
for x in states:
    print(x)
