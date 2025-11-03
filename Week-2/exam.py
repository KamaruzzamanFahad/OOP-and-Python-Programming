class Exam:
    def __init__(self, merk, subject, date, duration):
        self.merk = merk
        self.subject = subject
        self.date = date
        self.duration = duration

    def getMark(self):
        return f"Exam Merk: {self.merk}, Subject: {self.subject}, Date: {self.date}, Duration: {self.duration} hours"
    def isFailed(self, score):
        return score < 50
    def isPassed(self, score):
        return score >= 50
exam1 = Exam("Midterm", "Mathematics", "2024-10-15", 2)
exam2 = Exam("Final", "Science", "2024-12-20", 3)
print(exam1.getMark())
print("Exam 1 Passed:", exam1.isPassed(75))
print("Exam 1 Failed:", exam1.isFailed(40))
print(exam2.getMark())
print("Exam 2 Passed:", exam2.isPassed(45))
print("Exam 2 Failed:", exam2.isFailed(45))
    