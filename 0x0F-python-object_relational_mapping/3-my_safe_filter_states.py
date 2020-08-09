#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
        if ";" not in argv[4]:
            query = "SELECT * FROM states \
            WHERE states.name = '{}' \
            ORDER BY states.id"

            cur.execute(query.format(argv[4]))
            print(*cur.fetchall(), sep="\n")
