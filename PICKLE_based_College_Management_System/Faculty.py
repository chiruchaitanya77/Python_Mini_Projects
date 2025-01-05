import pickle


class student_info:
    def __init__(self, __name, __password, __roll, __marks):
        self.__name=__name
        self.__password=__password
        self.__roll=__roll
        self.__marks=__marks

    def set_name(self, __name):
        self.__name=__name
    def get_name(self):
        return self.__name
    def set_password(self, __password):
        self.__password=__password
    def get_password(self):
        return self.__password
    def set_roll(self, __roll):
        self.__roll=__roll
    def get_roll(self):
        return self.__roll
    def set_marks(self, __marks):
        self.__marks=__marks
    def get_marks(self):
        return self.__marks
    def get_teacher_info(self):
        return (f'Student Name: {self.get_name()}\nPassword: {self.get_password()}\nID: {self.get_roll()}')

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

class teacher():

    def t_login(self):
        print("\n<------ Faculty Login Menu ------>")
        rl = input("Enter Faculty UserName: ")
        pas = int(input("Enter Faculty ID: "))
        with open("teachers.pickle", "rb") as f:
            try:
                while True:
                    tt = pickle.load(f)
                    if tt._teacher_info__username == rl and tt._teacher_info__id == pas:
                        self.teacher_menu()
                    else:
                        print("Wrong username or id")
                        self.t_login()
            except EOFError:
                print("Roll number not found.")
                self.t_login()

    def teacher_menu(self):
        while True:
            print("\n<------ Teacher Menu ------>")
            print("1. Add Student")
            print("2. Add Student Marks")
            print("3. Show Student Details")
            print("4. Exit")
            c = choice()
            if c == 1:
                self.student_register()
            elif c == 2:
                roll = int(input("Enter Student Roll No.: "))
                marks = int(input("Enter Student Marks: "))
                self.append_marks(roll, marks)
            elif c == 3:
                with open("student.pkl", "rb") as f:
                    while True:
                        try:
                            data = pickle.load(f)
                            print("Roll: ", data._student_info__roll)
                            print("Username: ", data._student_info__name)
                            print("Password: ", data._student_info__password)
                            print("Marks: ", data._student_info__marks)
                        except EOFError:
                            break
            elif c == 4:
                import main
                main.m.main_menu()
                break
            else:
                print("Invalid choice. Please enter a valid number.")

    def student_register(self):
        import os
        while True:
            uNs = input("Enter Student Name or d to quit: ")
            if uNs == "d":
                break
            else:
                with open("student.pkl", "rb+") as f:
                    if os.path.getsize("student.pkl") == 0:
                        break
                    else:
                        data = pickle.load(f)
                        if data._student_info__name == uNs:
                            print("Name already exists. Please choose different Name.")
                            continue
                        else:
                            break
        while True:
            uPw = input("Enter Student Password: ")
            with open("student.pkl", "rb+") as f:
                try:
                    data = pickle.load(f)
                    if data._student_info__password == uPw:
                        print("Password already exists. Please choose different Password.")
                        continue
                    else:
                        break
                except EOFError:
                    break
        while True:
            uId = int(input("Enter Student ID: "))
            with open("student.pkl", "rb+") as f:
                try:
                    data = pickle.load(f)
                    if data._student_info__roll == uId:
                        print("ID already exists. Please choose different ID.")
                        continue
                    else:
                        break
                except EOFError:
                    break
        marks = None
        self.add_student(uNs, uPw, uId, marks)
        print("Student added successfully!")

        with open("student.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    print("Roll: ", data._student_info__roll)
                    print("Name: ", data._student_info__name)
                    print("Password: ", data._student_info__password)
                    print("Marks: ", data._student_info__marks)
                except EOFError:
                    break

    def add_student(self, name, password, roll, marks):
        s = student_info(name, password, roll, marks)
        with open("student.pkl", "ab+") as f:
            pickle.dump(s, f)

    def remove_student(self, __name):
        uN = input("Enter Student Name: ")
        with open("student.pkl", "rb") as f:
            data = pickle.load(f)
            data = [entry for entry in data if entry["name"] != uN]
        print("Updated data saved successfully!")
        print(data)
        with open('student.pkl', 'wb') as f:
            pickle.dump(data, f)
        print("Updated data saved successfully!")

    # Function to append marks to a specific student
    def append_marks(self, roll, marks):
        students = []  # To store all student objects
        updated = False
        with open("student.pkl", "rb") as f:
            try:
                while True:
                    s = pickle.load(f)
                    if s._student_info__roll == roll:
                        s._student_info__marks = marks  # Append marks
                        updated = True
                    students.append(s)
            except EOFError:
                pass
        if not updated:
            print(f"Roll number {roll} not found.")
            return
        # Rewrite the updated data to the pickle file
        with open("student.pkl", "wb") as f:
            for i in students:
                pickle.dump(i, f)

        print(f"Marks have been successfully updated for roll number {roll}.")

t = teacher()
t.t_login()