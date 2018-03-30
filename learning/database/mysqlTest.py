import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
cursor.execute('select * from usermaster where name = %s', ('name_mysql',))
values = cursor.fetchall()
print(values)
