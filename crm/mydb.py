import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='26th_avenue',
    passwd='password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE app_db")

print('All Done!!')