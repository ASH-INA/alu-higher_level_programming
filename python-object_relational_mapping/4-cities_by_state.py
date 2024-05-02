#!/usr/bin/python3
"""
This script lists all cities from the 'cities' table of the specified database,
ordered by city ID, along with their corresponding state names.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    c = db.cursor()

    # Execute the SQL query to fetch all cities and their corresponding state names
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
               FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
               ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")

    # Print the cities along with their corresponding state names
    [print(city) for city in c.fetchall()]
