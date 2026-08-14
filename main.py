
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
        super().__init__(subject, score, title, max_score, due_date, "homework")

class Exam(Assignment):
    def __init__(self, subject, score, title, max_score, due_date):
        super().__init__(subject, score, title, max_score, due_date, "exam")
               
#exam1 = Exam("Math", 85, "Midterm Exam", 100, date(2023, 10, 15))   

class GradeTracker:
    def __init__(self):
        self.assignments = []
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment added: {assignment.subject} - {assignment.score}")
    def list_assignments(self):
        if self.assignments == []:
            print("No assignments found.")
        else:
            for assignment in self.assignments:
                print(f"{assignment.subject} - {assignment.score} - {assignment.title} - {assignment.due_date} - {assignment.type}")
    def filter_assignments(self, subject=None, atype=None, due_date=None):
        filtered_assignments = self.assignments
        if subject:
            new_list = []                           # 1. start empty
            for assignment in filtered_assignments:  # 2. go through current list
                if assignment.subject == subject:    # 3. check the condition
                    new_list.append(assignment)       # 4. keep matches
            filtered_assignments = new_list           # 5. replace with the filtered result
        if atype:
            new_list = []                          
            for assignment in filtered_assignments:  
                if assignment.type == atype:    
                    new_list.append(assignment)       
            filtered_assignments = new_list           
        if due_date:
            new_list = []                          
            for assignment in filtered_assignments:  
                if assignment.due_date.startswith(due_date):  
                    new_list.append(assignment)      
            filtered_assignments = new_list           
        return filtered_assignments
    def show_summary(self):
        total_assignments = len(self.assignments)
        total_score = 0
        total_max_score = 0
        for assignment in self.assignments:
            total_score += assignment.score
            total_max_score += assignment.max_score
        if total_assignments > 0:
            average_score = total_score / total_max_score * 100
            print(f"Total Assignments: {total_assignments}, Average Score: {average_score:.2f}")
        else:
            print("No assignment found.")    
       


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