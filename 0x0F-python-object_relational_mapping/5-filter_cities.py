#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
   from sys import argv
   import MySQLdb

   with MySQLdb.connect("localhost", argv[1], argv[2], argv[3]) as cur:
      if ";" not in argv[4]:
          query = "SELECT cities.name \
                   FROM cities \
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name = '{}' \
                   ORDER BY cities.id"

          cur.execute(query.format(argv[4]))
          rec = cur.fetchall()
          record = []
          [record.append(i) for i in rec if i not in record]
          print(", ".join([r[0] for r in record]))
