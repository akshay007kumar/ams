import mysql.connector
try:
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='admin',
            database='studentAttend'
        )

    cursor = con.cursor()
    cursor.execute('SELECT * FROM admin')
    adminList = cursor.fetchall()
    cursor.execute('SELECT * FROM teacher')
    teacherList = cursor.fetchall()
    cursor.execute('SELECT * FROM student')
    studentList = cursor.fetchall()

except Exception as e:
    print('Database Error: ',e)

