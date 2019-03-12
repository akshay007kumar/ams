# Presentation Layer of Assignment Management System
import BLL
from myDB import *



def main():
    print('*** AMS ***')



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error: ', e)
    finally:
        if con.is_connected():
            con.close()


