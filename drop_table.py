import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("Databse connected successful!!")
cursor = connection.cursor()
try:
    sql_delete="DROP TABLE COMPANY1"
    cursor.execute(sql_delete)
    print('your table deleted')
except Exception as e:
    print(e)