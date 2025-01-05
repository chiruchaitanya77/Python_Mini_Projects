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

from Student import s

class teacher():
    def __init__(self):
        self.data = {1: "t1", 2: "t2", 3: "t3"}

    def t_login(self):
        while True:
            try:
                tid = int(input("Please enter Teacher Login id: "))
                break
            except ValueError:
                print("Invalid input. Please valid number.")
                continue
        tname = input("Please enter Teacher Login name: ")

        if tid in t.data and tname == t.data[tid]:
            print(f'\nWelcome {t.data[tid]}')
            t.teacher_menu()
        else:
            print("Wrong id or name")
            t.t_login()

    def teacher_menu(self):
        while True:
            print("\nFaculty Menu:")
            print("1. Add Student")
            print("2. Show Student Details")
            print("3. Add Student Marks")
            print("4. Exit")
            c = choice()
            if c == 1:
                t.s_register()
            if c == 2:
                for key, value in s.sdata.items():
                    print("-" * 30)
                    print(f"Student name: {value} \nStudent Id: {key}")
                t.teacher_menu()
            if c == 3:
                student_id = int(input("Enter Student ID: "))
                if student_id in s.sdata:
                    if student_id in s.smdata and s.smdata[student_id] > 0:
                        print(f"Marks already allotted for Student ID {student_id}: {s.smdata[student_id]}")
                    else:
                        marks = int(input("Enter Marks: "))
                        print(t.add_marks(student_id, marks))
                else:
                    print(f"Student ID {student_id} does not exist in the student list (sdata).")
                    continue
                t.teacher_menu()
            if c == 4:
                print(">>>> Exiting Management System >>>>")
                import mn
                mn.m.main_menu()

    def add_student(self, id, name):
        s.sdata[id] = name

    def add_marks(self, id, marks):
        s.smdata[id] = marks
        return f"Marks {marks} added successfully for Student ID {id}"

    def s_register(self):
        while True:
            name = input("Enter student name or d to quit: ")
            if name.lower() == "d":
                print(">>>> Redirecting to Main menu >>>>")
                t.teacher_menu()
                return
            try:
                id = int(input("Enter Student ID: "))
                if id in s.sdata:
                    print("ID already exists. Please choose different ID.")
                else:
                    self.add_student(id, name)
                    print(f"Student {name} with ID {id} added successfully!\n")
            except ValueError:
                print("Invalid input. Please valid ID.")

t = teacher()