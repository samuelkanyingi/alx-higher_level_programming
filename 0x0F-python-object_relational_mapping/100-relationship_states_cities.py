#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Create the State "California"
    california = State(name="California")

    # Create the City "San Francisco" and link it to the State
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Add the State and City objects to the session
    session.add(california)

    # Commit the session to persist the changes to the database
    session.commit()

    # Close the session
    session.close()
