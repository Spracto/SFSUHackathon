from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="civicHack"

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/cityLookup', methods=['post'])
def cityLookup():
	city = request.form['city']
	print city
	return redirect("/")

app.run(debug=True)
