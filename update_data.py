import pymysql.connections
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("Databse connected successful!!")
cursor = connection.cursor()
try:
    update_data="UPDATE COMPANY SET COMPANY_NAME='DJ&sons' WHERE COMPANY_NAME='KB & sons' "
    cursor.execute(update_data)
    print('your table data updated')
except Exception as e:
    print(e)