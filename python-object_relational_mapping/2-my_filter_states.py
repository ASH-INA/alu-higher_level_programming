#!/usr/bin/python3
"""
This script displays all values in the 'states' table of the specified database
whose name matches the state name supplied as an argument.

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> 
    <database_name> <state_name_searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    c = db.cursor()

    # Execute the SQL query to fetch states matching the supplied name
    c.execute("SELECT * \
               FROM `states` \
               WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Print the matching states
    [print(state) for state in c.fetchall()]
