#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
   from sys import argv
   import MySQLdb

   with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
       cur.execute("SELECT * FROM states ORDER BY states.id")
       print(*[re for re in cur if re[1].startswith('N')], sep="\n")
