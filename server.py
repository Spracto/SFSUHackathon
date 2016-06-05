from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import psycopg2
import psycopg2.extras
import sys

app.secret_key ="civicHack"

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/cityLookup', methods=['post'])
def cityLookup():
	try:
	    conn = psycopg2.connect("dbname='sfsuhackathon' user='postgres' host='localhost' password='#2002Civic'")
	    print "heyyyy that pretty cool"
	except:
	    print "I am unable to connect to the database"
	cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
	try:
	    SQL = "SELECT * FROM hackathon WHERE address LIKE (%s);"
	    data = ("255 RED%",)
	    cur.execute(SQL, data)
	except:
	    print "cannot execute"

# rows = cur.fetchall()

app.run(debug=True)
