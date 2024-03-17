#!/usr/bin/python3
""" types state withe name given 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engcre = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engcre)
    Session = sessionmaker(bind=engcre)
    ses = Session()
    for n in ses.query(State).filter(State.name.like('%a%')):
        ses.delete(n)
    ses.commit()
