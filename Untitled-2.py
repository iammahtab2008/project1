class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname, age, score):
        super().__init__(fname, lname)
        self.age = age
        self.score = score

student = Student("mahtab", "mohajeri", 17, 100)

print(f"name= {student.fname} {student.lname}")
print(f"score= {student.score}")
