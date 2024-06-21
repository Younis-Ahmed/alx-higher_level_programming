#!/usr/bin/python3
"""
takes in an argument and displays all values in the states\
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name='{}'
                ORDER BY cities.id ASC""".format(argv[-1]))

    print(', '.join(row[0] for row in cur.fetchall()))
    cur.close()
