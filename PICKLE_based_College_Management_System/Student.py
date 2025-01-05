import pickle
from Faculty import student_info

def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")

class student:
    def __init__(self):
        self.sdata = {1: "s1", 2: "s2", 3: "s3"}

    def s_login(self):
        print("\n<------ Student Login Menu ------>")
        rl = int(input("Enter roll number: "))
        pas = int(input("Enter password(Hint : Roll number): "))
        with open("student.pkl", "rb") as f:
            try:
                while True:
                    s = pickle.load(f)
                    if s._student_info__roll == rl and pas == rl :
                        self.student_menu()
                    else:
                        print("Wrong roll number or password")
                        self.s_login()
            except EOFError:
                print("Roll number not found.")
                self.s_login()

    def student_menu(self):
        while True:
            print("\nStudent Menu:")
            print("1. View Marks")
            c = choice()
            if c == 1:
                self.view_marks()

    def view_marks(self):
        rl = int(input("Enter roll number: "))
        with open("student.pkl", "rb") as f:
            try:
                while True:
                    s = pickle.load(f)
                    if s._student_info__roll == rl :
                        print(f"Roll number: {s._student_info__roll}")
                        print(f"Name: {s._student_info__name}")
                        print(f"Marks: {s._student_info__marks}")
                        break
            except EOFError:
                print("Roll number not found.")

s = student()