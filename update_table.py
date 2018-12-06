import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("Databse connected successful!!")
cursor = connection.cursor()

try:
    rename_table="ALTER TABLE COMPANY RENAME TO DETAILS"
    cursor.execute(rename_table)
    print('Table updated')
except Exception as e:
    print(e)