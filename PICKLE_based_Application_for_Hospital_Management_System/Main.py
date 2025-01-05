from Management import *
from Doctor import *

class main:
    def choice(choice=None):
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

    def main(self):
        print("#-#-#-#-#---- Welcome to PICKLE Application based Hospital Management System ----#-#-#-#-#")
        print("1. Management")
        print("2. Doctor")
        print("3. Staff")
        print("4. Patient")
        c = self.choice()
        if c == 1:
            import Management
            Management.m.m_login()
        elif c == 2:
            import Doctor
            Doctor.d.d_login()
        elif c == 3:
            import Staff
            Staff.s.s_login()
        elif c == 4:
            import Patient
            Patient.p.p_login()
        else:
            print("Invalid choice. Exiting...")

m = main()
m.main()
