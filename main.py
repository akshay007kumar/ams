# Presentation Layer of Assignment Management System
from BLL import Student
from myDB import *



def main():
    print('*** AMS ***')
    while True:
        try:
            ch = input('''User Type:
        1. Admin
        2. Teacher
        3. Student
            your choise: ''')
            if ch == '1':
                print('Admin')
                for a in adminList:
                    print(a)

            elif ch == '2':
                print('Teacher')
                for t in teacherList:
                    print(t)

            elif ch == '3':
                print('Student')
                for s in studentList:
                    print(s)

            else:
                print('Invalid Input!')
        finally:
            ex = input('Wanna EXIT? Y/N: ')
            if ex == 'y' or ex == 'Y':
                break
















if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error: ', e)
    finally:
        if con.is_connected():
            con.close()


