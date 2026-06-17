import psycopg2

con = psycopg2.connect(
	host="localhost",
	database="marksheet",
	user="postgres",
	password="1234")

cur = con.cursor()

print("Database connected ")