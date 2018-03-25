import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
cursor.execute('select * from user where username = %s', ('yanchao',))
values = cursor.fetchall()
print(values)
