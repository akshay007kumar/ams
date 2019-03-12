import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='admin',
        database='studentAttend'
    )

except Exception as err:
    print('Error: ', err)

