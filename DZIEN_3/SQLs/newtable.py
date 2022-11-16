import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306, database="dbtestowa")

cursorObject = db.cursor()
table_student = "CREATE TABLE student(name varchar(255),nr_alb int);"
cursorObject.execute(table_student)

sql_st_data = "INSERT INTO student(name,nr_alb) values(%s,%s)"
val = ("Jan",2345)
cursorObject.execute(sql_st_data,val)
db.commit()
print(cursorObject.rowcount,"element osadzony")

db.close()
