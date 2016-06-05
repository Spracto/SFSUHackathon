#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)
import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='sfsuhackathon' user='postgres' host='localhost' password='#2002Civic'")
    # conn = psycopg2.connect("dbname='sfhackathon' user='rushabindi' host='localhost' password='password'")
    print "heyyyy that pretty cool"
except:
    print "I am unable to connect to the database"

# cur = conn.cursor()
curs = conn.cursor()

# try:
#     curs.execute("Select * FROM hackathon")
#     colnames = [desc[0] for desc in curs.description]
#     print colnames

cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

try:
    SQL = "SELECT * FROM hackathon WHERE address LIKE (%s);"
    data = ("255 RED%",)
    cur.execute(SQL, data)
except:
    print "cannot execute"

rows = cur.fetchall()
result = rows[0]['address']
print result
# print rows[0]['address']
# dict(rows)
# print rows
# for row in rows:



# cur.execute("SELECT address FROM hackathon WHERE address LIKE (%s)", (""))
# cur.execute("""SELECT address FROM hackathon WHERE address LIKE '255 RED ROCK WY%'""")
# cur.query("""SELECT address FROM hackathon WHERE address LIKE ''""")