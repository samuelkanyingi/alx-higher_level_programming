#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create the State object
    new_state = State(name="Louisiana")

    # Add the State object to the session
    session.add(new_state)

    # Commit the session to persist the changes to the database
    session.commit()

    # Print the new state id
    print(new_state.id)

    # Close the session
    session.close()
