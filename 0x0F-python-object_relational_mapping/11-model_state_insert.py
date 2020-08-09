#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="asd")

    session.add(newState)
    session.commit()

    record = session.query(State).all()

    print(len(record))

    session.close()