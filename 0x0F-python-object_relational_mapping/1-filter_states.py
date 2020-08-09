#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
        cur.execute("SELECT * FROM states ORDER BY states.id")

        for record in cur.fetchall():
            if record[1].startswith('N'):
                print(record)
