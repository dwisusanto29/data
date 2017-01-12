#!/usr/bin/env python
from __future__ import print_function
import sys
import pymysql
#import csv

dbServer='202.124.205.201'
dbPass='alvin'
dbSchema='db_dws'
dbUser='alvin'

#dbQuery="select * from dataperjampbTest.Orders;";
conn = pymysql.connect(host=dbServer, port=3306, user=dbUser, passwd=dbPass, db=dbSchema)

cur=conn.cursor()
cur.execute("select * from dataperjam")
#result=cur.fetchall()

#print(cur.description)
#print()
#c = csv.writer(open("temp.csv","wb"))
for row in cur:
    print (row)
 #   c.writerow(row)

cur.close()
conn.close()