import pymysql

db = pymysql.connect("localhost","root","root","testdb")
cursor = db.cursor()
cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()