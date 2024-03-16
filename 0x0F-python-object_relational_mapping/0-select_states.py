#!/usr/bin/python3
""" list all states from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    state = c.fetchall()
    for states in state:
        print(states)
    c.close()
    db.close()