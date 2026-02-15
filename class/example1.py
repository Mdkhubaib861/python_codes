class Student:
    def __init__(self, rollno, name, division):
        self.rollno = rollno
        self.name = name
        self.division = division

    def displaystudentdata(self):
        print(self.rollno, self.name, self.division)

s1 = Student(1, "Marco", "Final Year")
s1.displaystudentdata()
