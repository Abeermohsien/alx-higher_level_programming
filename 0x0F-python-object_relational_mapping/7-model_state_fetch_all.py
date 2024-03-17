#!/usr/bin/python3
"""link class"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engcre = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engcre)
    Session = sessionmaker(bind=engcre)
    sesscre = Session()
    for instance in sesscre.query(State).order_by(State.id):
        print(instance.id, instance.name, sepator=": ")
