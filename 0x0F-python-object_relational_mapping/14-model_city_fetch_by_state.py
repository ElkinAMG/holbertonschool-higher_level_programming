#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Session = sessionmaker(bind=engine)

    session = Session()

    record = session.query(City, State.name).join(State).filter(State.id == City.state_id).order_by(City.id).all()

    for re in record:
        print("{}: ({}) {}".format(re[1], re[0].id, re[0].name))

    session.close()
