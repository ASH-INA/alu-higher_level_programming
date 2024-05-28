#!/usr/bin/python3
"""
This script prints the first State object from the 'states' table of the
specified database.

Usage:
    ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
    <database_name>
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

    # Query the first State object ordered by its ID
    state = session.query(State).order_by(State.id).first()

    # Print the State object if found, otherwise print "Nothing"
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
