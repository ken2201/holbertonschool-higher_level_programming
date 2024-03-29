#!/usr/bin/python3
''' takes in arguments and displays all values '''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id",
                (sys.argv[4],))
    [print(states) for states in cur.fetchall()]
    cur.close()
    db.close()
