#!/usr/bin/env python
from __future__ import print_function
import sys
import pymysql
#import csv

dbServer='localhost'
dbPass='sayangku'
dbSchema='db_dws'
dbUser='root'

#dbQuery="select * from dataperjampbTest.Orders;";
conn = pymysql.connect(host=dbServer, port=3306, user=dbUser, passwd=dbPass, db=dbSchema)

cur=conn.cursor()
data = ('baru', '-1.234', '45.7');
sql = "INSERT INTO tb_lokasi(lokasi, lat, long) VALUES ('%s','%s','%s')";
cur.execute(sql, data);
conn.commit()
#cur.execute(,data)
#conn.commit();
#result=cur.fetchall()

#print(cur.description)
#print()
#c = csv.writer(open("temp.csv","wb"))
#
#for row in cur:
#    print (row)
 #   c.writerow(row)

cur.close()
conn.close()