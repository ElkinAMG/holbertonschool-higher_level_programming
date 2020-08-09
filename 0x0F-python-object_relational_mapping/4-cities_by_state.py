#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
   from sys import argv
   import MySQLdb

   with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
       query = "SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON states.id = cities.state_id \
                ORDER BY cities.id"

       cur.execute(query)
       print(*cur.fetchall(), sep="\n")
