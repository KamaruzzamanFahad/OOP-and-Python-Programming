from turtle import st


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers= {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def student_addmition(self, student):
        classnem = student.classroom.name
        self.classrooms[classnem].add_student(student)


    @staticmethod
    def calculate_greade(marks):
        if marks >=80 and marks <=100:
            return 'A+'
        elif marks >= 70 and marks <80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks <50:
            return 'C'
        elif marks >= 33 and marks <40:
            return 'D'
        else:
            return 'F'
    
    @staticmethod
    def gread_to_value(grade):
        grade_map={
            'A+': 5.0,
            'A': 4.0,
            'A-': 3.5,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_map[grade]

    @staticmethod
    def value_to_gread(value):
        if value >=4.5 and value <=5.0:
            return 'A+'
        elif value >=3.5 and value <4.5:
            return 'A'
        elif value >=3.0 and value <3.5:
            return 'A-'
        elif value >=2.5 and value <3.0:    
            return 'B'
        elif value >=2.0 and value <2.5:
            return 'C'
        elif value >=1.0 and value <2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self):
        print("All Students")

        result = ""
        for key, value in self.classrooms.items():
            result += (f"...{key.upper()} classroom students...\n")

            for student in value.students:
                result += f"{student.name} \n"
        print(result)


        print("All Subjects")
        subject = ''
        for key, value in self.classrooms.items():
            subject += f"... {key.upper()} classroom subjects \n"
            for sub in value.subjects:
                subject += f"{sub.name} \n"
        print(subject)

        print("Students Results")
        results = ''
        for key, value in self.classrooms.items():
            results += f"... {key.upper()} classroom results ... \n"
            for student in value.students:
                results += f"Student Name: {student.name} \n"
                for sub, grade in student.subject_grade.items():
                    results += f"Subject: {sub} - Grade: {grade} \n"
        print(results)
        return ""



