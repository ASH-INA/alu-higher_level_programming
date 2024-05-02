#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico" in the database hbtn_0e_6_usa.
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

    # Query the State object with id = 2 and change its name to "New Mexico"
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    # Commit the changes
    session.commit()
