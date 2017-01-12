import pymysql as dbapi
import sys
import csv

dbServer='202.124.205.201'
dbPass='alvin'
dbSchema='db_dws'
dbUser='alvin'

#dbQuery="select * from dataperjampbTest.Orders;";
conn = dbapi.connect(host=dbServer, port=3306, user=dbUser, passwd=dbPass, db=dbSchema)

#db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
cur=conn.cursor()
cur.execute("select * from dataperjam;")
result=cur.fetchall()

c = csv.writer(open("temp.csv","wb"))
for row in result:
    c.writerow(row)