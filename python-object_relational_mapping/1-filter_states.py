#!/usr/bin/python3
"""
This script lists all states with names starting with 'N'
from the specified database.

Usage:
    python3 script_name.py <username> <password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    c = db.cursor()

    # Execute the SQL query to fetch all states ordered by id
    c.execute("SELECT * FROM `states` ORDER BY `id`")

    # Print states whose names start with 'N'
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
