#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session class
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Add California state with San Francisco city to the database
    session.add(City(name="San Francisco", state=State(name="California")))

    # Commit the changes
    session.commit()
