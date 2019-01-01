import pymysql.connections

###Connect to the database
connection = pymysql.connect(host='localhost',user='root',password='',db='test')
print("connect successful!!")
cursor = connection.cursor()
#
#
sql = """CREATE TABLE COMPANY (

    ID INT NOT NULL AUTO_INCREMENT,
    COMPANY_NAME varchar(100) NOT NULL,
    DATE DATE NOT NULL,
    TOTAL CHAR(20) NOT NULL,
    PRIMARY KEY (ID)
);
   """
print('Table created succesfully ')

try:
    cursor.execute(sql)##for ecexute your query
except Exception as ex:
    print(ex)####print exception