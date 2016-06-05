import psycopg2
import psycopg2.extras

def dbConnector():
	conn = psycopg2.connect("dbname='sfhackathon' user='rushabindi' host='localhost' password='password'")
	# conn = psycopg2.connect("dbname='sfsuhackathon' user='postgres' host='localhost' password='#2002Civic'")
	return conn
