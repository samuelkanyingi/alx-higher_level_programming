#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

def search_states(username, password, database, state_name):
    """
    Function to display all values in the states table where name matches the given state_name.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): State name to search for

    Returns:
        None

    Prints:
        States from the states table where name matches the given state_name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()

    # Execute SQL query to retrieve states matching the given state_name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    states = cur.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)

