import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("connect successful!!")
cursor = connection.cursor()

cname='kushal & sons'
date='2000-03-14'
print(type(date))
total='8800'

try:
    sql = ("INSERT INTO COMPANY1(ID,COMPANY_NAME,DATE, TOTAL) VALUES (0,%s, %s, %s)")
    VALUES = (cname, date, total)
    cursor.execute(sql, VALUES)
    print('Your DATA inserted')
except Exception as e:
    print(e)
