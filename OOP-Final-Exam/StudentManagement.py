class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student_obj):
        cls.student_list.append(student_obj)

class Student:
    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"done: student {self.__name} (ID: {self.__student_id}) has been enrolled.")
        else:
            print(f"error: student {self.__name} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"done: student {self.__name} has dropped out.")
        else:
            print(f"error: Cannot drop. student {self.__name} is not currently enrolled.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id} | Name: {self.__name} | Department: {self.__department} | Status: {status}")

    def get_student_id(self):
        return self.__student_id


student1 = Student("01", "fahad", "cse", is_enrolled=False)
student2 = Student("02", "khan", "eee", is_enrolled=True)
student3 = Student("03", "hasan", "python", is_enrolled=False)

while True:
    print("\n--- Student Management System ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\n--- Student List ---")
        if not StudentDatabase.student_list:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()
    
    elif choice == '2':
        s_id = input("Enter Student ID for enroll: ")
        found = False
        for student in StudentDatabase.student_list:
            if student.get_student_id() == s_id:
                student.enroll_student()
                found = True
                break
        if not found:
            print("error: Invalid Student ID.")
            
    elif choice == '3':
        s_id = input("Enter Student ID for drop: ")
        found = False
        for student in StudentDatabase.student_list:
            if student.get_student_id() == s_id:
                student.drop_student()
                found = True
                break
        if not found:
            print("error: invalid student ID.")
            
    elif choice == '4':
        print("Exiting the system.")
        break
    
    else:
        print("invalid choice. please try 1 to 4.")