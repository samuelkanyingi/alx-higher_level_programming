#!/usr/bin/env python3
"""
Deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa
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

    # Query the database to get all State objects with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in states:
        session.delete(state)

    # Commit the session to persist the changes to the database
    session.commit()

    # Close the session
    session.close()
