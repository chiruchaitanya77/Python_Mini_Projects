'''
4. Patient Module
    - PreDefine Registration values
        - UserName
        - Password
    1. Login to Patient System
        - Login with UserName and Password
        - Show Welcome to Patient Home Page Message
        - Login Patient
                - Successfully Login to Patient Account
                - Welcome to <Patient Name> Message
                - After Login Show Main Menu
                    - Main Menu
                        1. Book an Appointment with Doctor
                            - Enter Patient Name
                            - Enter Problem
                            - Mobile Number
                          - Show Successfully Booked Appointment Details
                        2. Health Report
                            - Staff Updated Report (Solved/Not Solved)
                        3. Exit Patient System
                            - Redirect to Main Application Page
'''

def choice():
    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            return user_choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")

class Patient:
    def __init__(self):
        self.p_app = {'Pn1': ['Prob1', '123123', 'Waiting', 'Doc Not Assigned'], 'Pn2': ['Prob2', '345345', 'Waiting', 'Doc Not Assigned']}

    def login(self):
        print("\n<----------Patient Login Page---------->")
        p.uN = get_non_empty_input("Enter Patient UserName: ")
        p.Pd = get_non_empty_input("Enter Patient Password: ")
        if p.uN == "p" and p.Pd == "ptp":
            print("Successfully Login Patient Account \n")
            p.patient_menu()
        else:
            print("Invalid login credentials. Please try again")
            p.login()

    def patient_menu(self):
        if not hasattr(self, "patient"):
            self.p_app = {}
        print("\n<---------- Welcome to Patient Main Page ---------->")
        print("1. Book an Appointment with Doctor")
        print("2. Health Report")
        print("3. Exit Patient System")
        c = choice()
        if c == 1:
            while True:
                Pname = get_non_empty_input("Enter Patient Name :")
                prob = get_non_empty_input("Enter Problem :")
                Pstat = "Waiting"
                doctor_id = None
                try:
                    Pmobile = int(input("Enter your Mobile Number: "))
                    print("\n-------( Show Successfully Booked Appointment Details )-------")
                    self.p_app[Pname] = [prob, Pmobile, Pstat, doctor_id]
                    print(f"Patient Name: {Pname} \nProblem: {prob} \nMobile Number: {Pmobile} \nStatus: {Pstat} \nDoctor ID: {doctor_id}")
                    p.patient_menu()
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        if c == 2:
            pass
        if c == 3:
            print("\n<------ Exiting Patient System ------>")
            __import__("com").main_menu()

    def get_p_app(self):
        for Pname, details in p.p_app.items():
            return (f"Name: {Pname} \nProblem: {details[0]} \nMobile No: {details[1]} \nStatus: {details[2]} \nDoctor ID: {details[3]}")

p = Patient()
