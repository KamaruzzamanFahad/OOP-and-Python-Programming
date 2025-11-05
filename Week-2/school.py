from re import S


class Student:
    def __init__(self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id
    def __repr__(self):
        return f"Student(Name: {self.name}, Class: {self.cls}, ID: {self.id})"

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f"Teacher(Name: {self.name}, Subject: {self.subject}, ID: {self.id})"
    
class School:
    def __init__(self, name):
        self.name = name
        self.students =[]
        self.teachers = []

    def add_Teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500 :
            return "Insufficient fee. Enrollment failed."
        else:
            id = len(self.students) + 1
            student = Student(name, 'c', id)
            self.students.append(student)
            return f"Enrollment successful! Student ID: {id} extra money: ${fee - 6500}"
    def __repr__(self):
        print("for students:")
        for student in self.students:
            print(student)
        print("for teachers:")
        for teacher in self.teachers:
            print(teacher)
        return f"School(Name: {self.name}, Total Students: {len(self.students)}, Total Teachers: {len(self.teachers)})"
    
        
# aliya = Student("Aliya", 9, 5)
# print(aliya)

phitron = School("Phitron")
phitron.enroll("Aliya", 3000)
phitron.enroll("Babu", 6000)
phitron.enroll("Kalam", 8000)
phitron.enroll("Jamal", 7000)

phitron.add_Teacher("Mr. X", "Math")
phitron.add_Teacher("Ms. Y", "Science")
phitron.add_Teacher("Dr. Z", "English")

print(phitron)