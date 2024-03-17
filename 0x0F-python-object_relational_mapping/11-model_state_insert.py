#!/usr/bin/python3
"""type state object"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_new = State(name='Louisiana')
    session.add(state_new)
    instance_new = session.query(State).filter_by(name='Louisiana').first()
    print(instance_new.id)
    session.commit()
