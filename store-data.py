"""
Code to store yahoo finance csv data 
in a postgresql database table
using psycopg2 and csv module
"""
import psycopg2
import csv

def storeCSVRow(rowList,cur):
    strQuery="insert into yahoofinancedata\
     values('%s','%s','%s','%s','%s','%s','%s')"\
     %(rowList[0],rowList[1],rowList[2],rowList[3],\
     rowList[4],rowList[5],rowList[6])
    cur.execute(strQuery)
def storeCSVData(cur):
    with open("table.csv","rb") as yahoocsvfile:
        rdr=csv.reader(yahoocsvfile)
        for row in rdr:
            print "storing row: "+str(row)
            storeCSVRow(row,cur)


conn=psycopg2.connect(database="sample",
                user="postgres",
                password="Goodguygordon13130#",
                host="127.0.0.1",
                port="5432")

cur = conn.cursor()
storeCSVData(cur)
conn.commit()
print("changes commited to database successfully!")
conn.close()
