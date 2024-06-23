#!/usr/bin/python3

"""script that lists all State from database"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    [print(f'{i.name}: ({j.id}) {j.name}')
     for i, j in session.query(State, City)
        .join(City, City.state_id == State.id)]
