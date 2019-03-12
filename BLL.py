# Bussiness Logic Layer of Attendance Management System


class Student:

    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.gender = None
        self.date_of_birth = None
        self.age = None
        self.address = None
        self.email = None
        self.course_id = None
        self.batch_id = None

    def add_student(self, id1, fname, lname, gen, dob, age, addr, email, cid, bid):
        self.id = id1
        self.firstname = fname
        self.lastname = lname
        self.gender = gen
        self.date_of_birth = dob
        self.age = age
        self.address = addr
        self.email = email
        self.course_id = cid
        self.batch_id = bid






class Teacher(Person): pass


class Attendence: pass


class Batch: pass


class Course: pass

