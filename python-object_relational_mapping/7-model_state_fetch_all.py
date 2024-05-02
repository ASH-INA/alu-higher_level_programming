#!/usr/bin/python3
"""
This script lists all State objects from the 'states' table of the specified database.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session class
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query and print all State objects ordered by their ID
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
