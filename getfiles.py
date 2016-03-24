import os
import pymysql #Python 3.4: $pip install PyMySQL

HOST='localhost'
PORT=3306
USER='root'
PASSWORD=''
DATABASE='configFileDB'

DEST_PATH=str(input("Enter with absolute destination path: "))
valid_Destination = os.path.isdir(DEST_PATH) and os.path.exists(DEST_PATH)
if not valid_Destination
    print("The following path {} is not valid.".format(DEST_PATH))
    return

connection = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DATABASE)

cursor = connection.cursor()

cursor.execute("select configName, configContent from configFiles limit 1;")

for row in cursor:
    fileName = row[0]
    fileContent = row[1]

    with open(DEST_PATH + fileName, 'w') as f:
        f.write(fileContent.replace('ip', 'domain').replace('absPathOnSrv', DEST_PATH))

cursor.close()
connection.close()

