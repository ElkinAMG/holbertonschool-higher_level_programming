#!/usr/bin/python3
"""
Write a script that lists all states from database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
        cur.execute("SELECT * FROM states ORDER BY states.id;")
        print(*cur.fetchall(), sep="\n")
