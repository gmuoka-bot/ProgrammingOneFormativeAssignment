
from datetime import date, datetime
subjects = ["Math", "Science", "History", "English", "Art"]
score = (0, 100)
types = ["exam", "homework"]
summary = {"total_assignments": 0, "total_exams": 0, "average_score": 0.0}, {"total_subjects": 0, "total_score": 0}

class Assignment:                        #the class holds the attributes of an assignment, including subject, score, title, max_score, due_date, and type.
    def __init__(self, subject, title, max_score, score, due_date, atype):
        self.subject = subject.lower().strip()          # ensures that the subject is always stored in lowercase and withouttrailing spaces
        self.max_score = max_score
        self.score = score
        self.title = title
        self.due_date = due_date
        self.type = atype                  

class Homework(Assignment):
    def __init__(self, subject, title, max_score, score, due_date):
        super().__init__(subject, title, max_score, score, due_date, "homework")        # homework is automatically set as the type for homework assignments

class Exam(Assignment):
    def __init__(self, subject, title, max_score, score, due_date):
        super().__init__(subject, title, max_score, score, due_date, "exam")            # exam is automatically set as the type for exam assignments
               

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
            new_list = []                                         # 1. start empty
            for assignment in filtered_assignments:                 # 2. go through current list
                if assignment.subject == subject.lower().strip():         # 3. check the condition and ensures capitalization and whitespace don't affect the filtering
                    new_list.append(assignment)                              # 4. keep matches
            filtered_assignments = new_list                              # 5. replace with the filtered result
        if atype:
            new_list = []                          
            for assignment in filtered_assignments:  
                if assignment.type == atype:    
                    new_list.append(assignment)       
            filtered_assignments = new_list           
        if due_date:                                               #due_date in format "YYYY-MM" for filtering by month
            new_list = []                          
            for assignment in filtered_assignments:  
                if assignment.due_date.startswith(due_date):     #to match the month of the due_date, we used .startswith()
                    new_list.append(assignment)      
            filtered_assignments = new_list           
        return filtered_assignments
    def show_summary(self):                                #calcutes avg score and total assignments
        total_assignments = len(self.assignments)
        total_max_score = 0
        total_score = 0
        for assignment in self.assignments:
           total_max_score += assignment.max_score
           total_score += assignment.score
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
    while True:                                       # so the functions keep running until the user chooses to exit
        print("1. Add homework","\n" 
     "2. Add exam scores", "\n"
     "3. List assignments", "\n"
     "4. Filter (by subject/ type/ month)","\n"
     "5. Show summary", "\n"
     "0. Exit")
        choice = input("Choose an option:")
        if choice == "1":
            homework = Homework(subject="", title="", max_score=0.0, score=0.0, due_date="")            # created a new instance of Homework this allows me store the details of the homework assignment that the user adds.
            homework.subject = input("Enter subject: ")
            homework.title = input("Enter title: ")
            homework.max_score = float(input("Enter max score: "))
            homework.score = float(input("Enter score (0-100): "))
            while homework.max_score < homework.score:                                              # ensures that the score is never greater than the max score
                print("Score cannot be greater than max score. Please enter a valid score.")
                homework.score = float(input("Enter score (0-100): "))
            homework.due_date = input("Enter due date (YYYY-MM-DD): ")
            tracker.add_assignment(homework)
        elif choice == "2":
            exam = Exam(subject="", title="", score=0.0, max_score=0.0, due_date="")            # created a new instance of Exam which will store the details of the exam that the user adds.
            exam.subject = input("Enter exam subject: ")
            exam.title = input("Enter exam title: ")
            exam.max_score = float(input("Enter max score: "))
            exam.score = float(input("Enter exam score (0-100): "))
            while exam.max_score < exam.score:
                print("Score cannot be greater than max score. Please enter a valid score.")
                exam.score = float(input("Enter exam score (0-100): "))
            exam.due_date = input("Enter exam date (YYYY-MM-DD): ")
            tracker.add_assignment(exam)
        elif choice == "3":
            tracker.list_assignments()
        elif choice == "4":                                                     # It prompts the user for their choice and then calls the filter_assignments method of the GradeTracker class with the appropriate parameters. 
            filter_choice = input("Filter by subject, type, or month? (subject/type/month): ")
            if filter_choice == "subject":
                subject = input("Enter subject to filter by: ")
                filtered = tracker.filter_assignments(subject=subject)
                if filtered == []:                                               # provides feedback to the user if no assignments match the filter criteria.
                    print(f"No assignments found for subject: {subject}")
                else:    
                    for assignment in filtered:
                        print(f"{assignment.subject} - {assignment.score} - {assignment.title} - {assignment.due_date} - {assignment.type}")
            elif filter_choice == "type":
                atype = input("Enter type to filter by (homework/exam): ")
                filtered = tracker.filter_assignments(atype=atype)
                if not filtered:
                    print(f"No assignments found for type: {atype}")
                else:    
                    for assignment in filtered:
                        print(f"{assignment.subject} - {assignment.score} - {assignment.title} - {assignment.due_date} - {assignment.type}")
            elif filter_choice == "month":
                month = input("Enter month to filter by (YYYY-MM): ")
                filtered = tracker.filter_assignments(due_date=month)
                if not filtered:
                    print(f"No assignments found for month: {month}")
                else:
                    for assignment in filtered:
                        print(f"{assignment.subject} - {assignment.score} - {assignment.title} - {assignment.due_date} - {assignment.type}")    
            else:
                print("Invalid filter choice.") 
        elif choice == "5":
            tracker.show_summary()
        elif choice == "0":                                      #exits the program when the user chooses to exit the program.
                print(f"Exiting program. Goodbye, {student}!")
                break
        else:                                                   # handles invalid choices by prompting the user to try again.
            print("Invalid choice. Please try again.")
    
   
student_success_tracker()