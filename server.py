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
	    # print "heyyyy that pretty cool"
	except:
	    print "I am unable to connect to the database"
	cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
	try:
		SQL = "SELECT * FROM hackathon WHERE address LIKE (%s);"
		# print request.form['city']
		userCity = request.form['city'].upper()
		data = (userCity + "%",)
		print data
		cur.execute(SQL, data)
		rows = cur.fetchall()
		if rows == []:
			errors = {
				'error' : "address not in database"
			}
			return render_template('result.html', result=errors)
		else:
			print rows
			# address = rows[0]['address']
			# status = rows[0]['status']
			result = {
				'address' : rows[0]['address'],
				'status' : rows[0]['status'],
				'notice' : rows[0]['notice'],
				'formRec' : rows[0]['sc_rcvd'],
				'formComp' : rows[0]['sc_comp'],
				'lot' : rows[0]['lot'],
				'tier' : rows[0]['tier'],
				'inOrOut' : rows[0]['inOrOut'],
				'optEvalRec' : rows[0]['opt_eval'],
				'block' : rows[0]['block']
			}
			print result
			# print "Hey this is what came back"+session['city']
			return render_template('result.html', results=result)
	except:
	    print "cannot execute"

@app.route('/reset', methods=['post'])
def reset():
	return redirect('/')

# rows = cur.fetchall()

app.run(debug=True)
