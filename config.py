#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='sfsuhackathon' user='postgres' host='localhost' password='#2002Civic'")
    # conn = psycopg2.connect("dbname='sfhackathon' user='rushabindi' host='localhost' password='password'")
    print "heyyyy that pretty cool"
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
curs = conn.cursor()

try:
    curs.execute("Select * FROM hackathon")
    colnames = [desc[0] for desc in curs.description]
    print colnames
    
    SQL = "SELECT * FROM hackathon WHERE address LIKE (%s);"
    data = ("255 RED%",)
    cur.execute(SQL, data)

except:
    print "cannot execute"

rows = cur.fetchall()
print rows