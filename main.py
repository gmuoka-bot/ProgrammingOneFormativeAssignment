
from datetime import date, datetime
subjects = ["Math", "Science", "History", "English", "Art"]
score = (0, 100)
types = ["Exam", "Assignment", "Summary"]
summary = {"total_assignments": 0, "total_exams": 0, "average_score": 0.0}, {"total_subjects": 0, "total_score": 0}

class Assignment:
    def __init__(self, subject, score, title, max_score, due_date, atype):
        self.subject = subject
        self.score = score
        self.title = title
        self.max_score = max_score
        self.due_date = due_date
        self.type = atype

class Homework(Assignment):
    def __init__(self, subject, score, title, max_score, due_date):
        super().__init__(subject, score, title, max_score, due_date)
        self.type = "Homework"

class Exam(Assignment):
    def __init__(self, subject, score, title, max_score, due_date):
        super().__init__(subject, score, title, max_score, due_date)
        self.type = "Exam"        
exam1 = Exam("Math", 85, "Midterm Exam", 100, date(2023, 10, 15))   

def student_success_tracker(homework={}, exam=[], assignments=[], summary={}, exit=False):
    """
    This function tracks the success of a student based on their homework, exam, and assignment scores."""

# student = input("Enter student's names:")
#print(f"Hello, {student}! What would you like to do today?")
print("1. Add Assignment scores","\n" 
     "2. Add exam scores", "\n"
     "3. List Assignment", "\n"
     "4. Filter (by subject/ type/ date)","\n"
     "5. View summary student records", "\n"
     "0. Exit")
#choice = input("Choose an option:")
#if choice == "1":
    #assignment = input("Enter assignment subject and score (subject, score): ")
    #assignment.subject = input("Enter assignment subject: ")
    #assignment.score = float(input("Enter assignment score (0-100): "))
       #print(f"Assignment added: {assignment.subject} - {assignment.score}")  
# elif choice == "2":
#    exam = input("Enter exam subject and score (subject, score): ")
#    exam.subject = input("Enter exam subject: ")
#    exam.score = float(input("Enter exam score (0-100): "))    
#print(f"Exam added: {exam.subject} - {exam.score}")

#student_success_tracker(homework=[], exam=[], Assignment=[], summary={}, exit=False)