import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
cursor = connection.cursor()

cname='Kushal&Sons'
date='2022-03-14'
total='890800'

try:
    sql = ("INSERT INTO COMPANY(ID,COMPANY_NAME,DATE, TOTAL) VALUES (0,%s, %s, %s)")
    VALUES = (cname, date, total)
    cursor.execute(sql, VALUES)
    print('Your DATA inserted')
except Exception as e:
    print(e)


###For fetch table data fro database
# print("connect successful!!")
# k=cursor.execute('SELECT * FROM COMPANY')
# fet=cursor.fetchall()
# print(fet )
