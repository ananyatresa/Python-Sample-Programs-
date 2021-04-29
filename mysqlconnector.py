import mysql.connector
cnx=mysql.connector.connect(user='glitchy',password='3333',host='127.0.0.1',database='school')
cnx.close()
cursor=cnx.cursor
sql = "INSERT INTO customers (name, address) VALUES (%d, %d)"
val = [
  ('Peter', '4'),
  ('Amy', '2'),
  ('Hannah', '1'),
]
result=cursor.executemany(sql,val)
print (cursor.fetchall())
