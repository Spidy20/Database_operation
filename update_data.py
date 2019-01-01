import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("Databse connected successful!!")
cursor = connection.cursor()


try:
    update_data="UPDATE COMPANY SET DATE='2020-08-15' WHERE DATE='2000-03-14' "
    cursor.execute(update_data)
    print('your table data updated')
except Exception as e:
    print(e)