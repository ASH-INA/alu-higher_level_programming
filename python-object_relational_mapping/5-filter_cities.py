#!/usr/bin/python3
"""
This script displays all cities of a given state from the 'cities' table
of the specified database. It is designed to be safe from SQL injections.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name_searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    c = db.cursor()

    # Execute the SQL query to fetch all cities and their
    #corresponding state names
    c.execute("SELECT * FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
               ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")

    # Print the cities of the given state
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
