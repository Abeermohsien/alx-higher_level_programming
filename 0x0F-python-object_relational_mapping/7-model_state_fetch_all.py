#!/usr/bin/python3
"""link class"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engcre = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engcre)
    Session = sessionmaker(bind=engcre)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sepator=": ")
