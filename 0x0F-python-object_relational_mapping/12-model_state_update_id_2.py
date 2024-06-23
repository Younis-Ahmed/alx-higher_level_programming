#!/usr/bin/python3

"""script that prints the first State object from the database"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    filtered = session.query(State).filter(State.id == 2).one()
    filtered.name = "New Mexico"
    session.commit()
