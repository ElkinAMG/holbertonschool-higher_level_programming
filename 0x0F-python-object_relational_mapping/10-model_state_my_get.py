#!/usr/bin/python3
"""
Write a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Session = sessionmaker(bind=engine)

    session = Session()

    re = session.query(State).filter(State.name.contains(argv[4])).first()

    if re:
        print(re.id)
    else:
        print("Not found")

    session.close()
