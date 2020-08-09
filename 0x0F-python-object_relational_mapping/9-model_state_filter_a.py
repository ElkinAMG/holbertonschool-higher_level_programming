#!/usr/bin/python3
"""
Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
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

    record = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()

    for re in record:
        print("{}: {}".format(re.id, re.name))

    session.close()
