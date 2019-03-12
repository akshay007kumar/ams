class Person(object):
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.gender = None
        self.date_of_birth = None
        self.age = None
        self.address = None
        self.email = None

    def add(self, id1, fname, lname, gen, dob, age, addr, email):
        self.id = id1
        self.firstname = fname
        self.lastname = lname
        self.gender = gen
        self.date_of_birth = dob
        self.age = age
        self.address = addr
        self.email = email



class Student(Person):

    def __init__(self):
        self.course_id = None
        self.batch_id = None
        super(Student, self).__init__()

    def addStudent(self, id1, fname, lname, gen, dob, age, addr, email, cid, bid):
        self.course_id = cid
        self.batch_id = bid
        # DATABASE EXECUTE STATEMENT ??? HOW

        super().add(id1, fname, lname, gen, dob, age, addr, email)






class Teacher(Person): pass


class Attendence: pass


class Batch: pass


class Course: pass

