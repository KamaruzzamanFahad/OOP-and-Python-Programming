from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom


school = School("Abc", "Dhaka")
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
jamal = Student("Jamal", ten)
school.student_addmition(rahim)
school.student_addmition(karim)
school.student_addmition(jamal)


abul = Teacher("Abul")
babul = Teacher("Babul")
kabul = Teacher("Kabul")

bangla = Subject("Bangla", abul)
math = Subject("Math", babul)
english = Subject("English", kabul)

eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(english)
nine.add_subject(bangla)
nine.add_subject(math)
ten.add_subject(bangla)
ten.add_subject(english)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)


