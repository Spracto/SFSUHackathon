#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='sfsuhackathon' user='postgres' host='localhost' password='#2002Civic'")
    print "heyyyy that pretty cool"
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

try:
    SQL = "SELECT address FROM hackathon WHERE address LIKE (%s);"
    data = ("255 RED%",)
    cur.execute(SQL, data)
    # cur.execute("SELECT address FROM hackathon WHERE address LIKE (%s)", (""))
    # cur.execute("""SELECT address FROM hackathon WHERE address LIKE '255 RED ROCK WY%'""")
    # cur.query("""SELECT address FROM hackathon WHERE address LIKE ''""")
except:
    print "cannot execute"

rows = cur.fetchall()
for row in rows:
    print "  ", row[0]
