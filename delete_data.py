import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("Databse connected successful!!")
cursor = connection.cursor()
try:
    delete_data="DELETE FROM COMPANY WHERE ID='5' "
    cursor.execute(delete_data)
    print('Data Deleted')
except Exception as e:
    print(e)