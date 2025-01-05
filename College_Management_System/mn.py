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


class menu:
    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Management Login")
            print("2. Faculty Login")
            print("3. Student Login")
            print("4. Exit")
            c = choice()

            if c == 1:
                import Management
                Management.m.m_login()
            if c == 2:
                import Teacher
                Teacher.t.t_login()
            if c == 3:
                import Student
                Student.s.s_login()
            if c == 4:
                print(">>>> Exiting College Management System >>>>")
                exit()

m = menu()
m.main_menu()