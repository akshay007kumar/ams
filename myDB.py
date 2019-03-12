import mysql.connector

con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='admin',
        database='studentAttend'
    )

cursor = con.cursor(prepared=True)
