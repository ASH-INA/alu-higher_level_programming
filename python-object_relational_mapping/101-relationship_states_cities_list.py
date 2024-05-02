#!/usr/bin/python3
"""
Lists all States and corresponding Cities in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session class
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query and print all States and corresponding Cities
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
