#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create connection URL
    url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    # Create SQLAlchemy engine and session
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get all State objects containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')
                                         ).order_by(State.id).all()

    # Loop through the states and print the id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
