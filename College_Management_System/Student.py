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
        self.smdata = {1: 20, 2: 30, 3: 0}
        self.logged_in_student_id = None

    def s_login(self):
        while True:
            try:
                sid = int(input("Please enter Student Login id: "))
                break
            except ValueError:
                print("Invalid input. Please valid number.")
                continue
        sname = input("Please enter Student Login name: ")
        if sid in s.sdata and sname == s.sdata[sid]:
            self.logged_in_student_id = sid
            print(f'\nWelcome {s.sdata[sid]}')
            s.student_menu()
        else:
            print("Wrong id or name")
            s.s_login()

    def student_menu(self):
        while True:
            print("\nStudent Menu:")
            print("1.View Marks")
            print("2.Exit")
            c = choice()
            if c == 1:
                student_id = self.logged_in_student_id
                marks = s.smdata[student_id]
                print(f"Marks of Student {s.sdata[student_id]} is {marks}")
                s.student_menu()
            if c == 2:
                print(">>>> Exiting Management System >>>>")
                import mn
                mn.m.main_menu()
            else:
                print("Invalid choice. Please enter a valid number.")

s = student()
