#!/usr/bin/python
import datetime
import MySQLdb
dbhost = "localhost"
dbuser = "root"
dbpass = "sayangku22"
db = "db_dws" 

# Open database connection
db = MySQLdb.connect(dbhost,dbuser,dbpass,db )
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = '''INSERT INTO baru(jam, suhu, kelembaban) values(%s,%s,%s)'''
data = (today, 30.5, 40.6);
cursor.execute(sql,data)
# Commit your changes in the database
db.commit()

# disconnect from server
db.close()