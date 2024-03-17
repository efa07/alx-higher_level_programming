#!/usr/bin/python3
"""
takes an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
and safe from MySQL injections!
"""
import MySQLdb
from sys import argv

# should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # used to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
