import mysql.connector #pip install PyMySQL

config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("select * from Table")
    
for r in cursor:
    print(r)

cursor.close()
connection.close()