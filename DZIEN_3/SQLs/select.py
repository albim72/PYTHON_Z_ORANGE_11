import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306, database="dbtestowa")

cursorObject = db.cursor()

query = "SELECT name,nr_alb FROM student;"

cursorObject.execute(query)

wynik = cursorObject.fetchall()
print(type(wynik))

for x in wynik:
    print(x)

print("____________________________________________")
query2 = "SELECT * FROM student where nr_alb>=1000;"

cursorObject.execute(query2)

wynik2 = cursorObject.fetchall()
print(type(wynik2))

for x in wynik2:
    print(x)

db.close()

