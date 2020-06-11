class Student:
        def __init__(self, fname, lname, roll_num, standard):
            self.fname = fname
            self.lname = lname
            self.roll_num = roll_num
            self.standard = standard

        def fullname(self):
            return self.fname + ' ' + self.lname


student_1 = Student('Romit', 'Patel', '25', 'X')

print(student_1.fullname())
print(student_1.lname)
