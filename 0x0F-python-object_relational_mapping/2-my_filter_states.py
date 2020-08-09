#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
   from sys import argv
   import MySQLdb

   with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
       query = "SELECT * FROM states WHERE states.name = '{}' ORDER BY states.id"
       cur.execute(query.format(argv[4]))
       print(*cur.fetchall(), sep="\n")
