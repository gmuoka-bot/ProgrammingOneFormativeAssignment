
from datetime import date, datetime
subjects = ["Math", "Science", "History", "English", "Art"]
score = (0, 100)
types = ["exam", "homework"]
summary = {"total_assignments": 0, "total_exams": 0, "average_score": 0.0}, {"total_subjects": 0, "total_score": 0}

class Assignment:                        #the class holds the attributes of an assignment, including subject, score, title, max_score, due_date, and type.
    def __init__(self, subject, title, score, max_score, due_date, atype):
        self.subject = subject
        self.score = score
        self.title = title
        self.max_score = max_score
        self.due_date = due_date
        self.type = atype                  

class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "homework")        # homework is automatically set as the type for homework assignments

class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "exam")            # exam is automatically set as the type for exam assignments
               
#exam1 = Exam("Math", 85, "Midterm Exam", 100, date(2023, 10, 15))   

class GradeTracker:
    def __init__(self):
        self.assignments = []               # Sets up an empty list to hold all the assignments added.
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment added: {assignment.subject} - {assignment.score}")
    def list_assignments(self):
        if self.assignments == []:
            print("No assignments found.")
        else:
            for assignment in self.assignments:
                print(f"{assignment.subject} - {assignment.score} - {assignment.title} - {assignment.due_date} - {assignment.type}")
    def filter_assignments(self, subject=None, atype=None, due_date=None):               # so each filter is optional, we set default values to None
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
        if due_date:             #due_date in format "YYYY-MM" for filtering by month
            new_list = []                          
            for assignment in filtered_assignments:  
                if assignment.due_date.startswith(due_date):     #to match the month of the due_date, we used .startswith()
                    new_list.append(assignment)      
            filtered_assignments = new_list           
        return filtered_assignments
    def show_summary(self):                                #calcutes avg score and total assignments
        total_assignments = len(self.assignments)
        total_score = 0
        total_max_score = 0
        for assignment in self.assignments:
            total_score += assignment.score
            total_max_score += assignment.max_score
        if total_assignments > 0:                          #only calculates if theres at least one assignment
            average_score = total_score / total_max_score * 100
            print(f"Total Assignments: {total_assignments}, Average Score: {average_score:.2f}")
        else:
            print("No assignment found.")    
       


def student_success_tracker():
    """
    This function tracks the success of a student based on their homework, exam, and assignment scores."""
    tracker = GradeTracker()            # puts all new inputs into class GradeTracker
    student = input("Enter student's names:")
    print(f"Hello, {student}! What would you like to do today?")
    print("1. Add homework","\n" 
     "2. Add exam scores", "\n"
     "3. List assignments", "\n"
     "4. Filter (by subject/ type/ month)","\n"
     "5. Show summary", "\n"
     "0. Exit")
    choice = input("Choose an option:")
    if choice == "1":
        homework = Homework(subject="", title="", score=0.0, max_score=0.0, due_date="")            # created a new instance of Homework called homework. This allows me store the details of the homework assignment that the user adds.
        homework.subject = input("Enter subject: ")
        homework.title = input("Enter title: ")
        homework.score = float(input("Enter score (0-100): "))
        homework.max_score = float(input("Enter max score: "))
        homework.due_date = input("Enter due date (YYYY-MM-DD): ")
        print(f"Assignment added: {homework.subject} - {homework.score}")  


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

    # elif choice == "2":
    #     exam = Exam()            # created a new instance of Exam called exam. This allows me to store the details of the exam that the user adds.
    #     exam.subject = input("Enter exam subject: ")
    #     exam.score = float(input("Enter exam score (0-100): "))    
    #     print(f"Exam added: {exam.subject} - {exam.score}")
    # elif choice == "3":
    #     print("Listing all assignments:")
    # elif choice == "4":
    #     filter = input("Filter by subject, type, or month? (subject/type/month): ")  
    # elif choice == "5":
    #     print(student.show_summary())
    # else:
    #     print(f"Exiting program. Goodbye, {student}!")

student_success_tracker()