'''
# Application Based Hospital Management System
- Show Welcome to Application based Hospital Management System Message
    -Show Files in modules folder
        1. Management
        2. Doctor
        3. Staff
        4. Patient
1. Management Module
    - PreDefine Registration values
        - UserName
        - Password
    1. Login to Management System
        - Login with UserName and Password
        - Show Welcome to Management Home Page Message
        - Login Company
                - Successfully Login Company Account
                - After Login Show Main Menu
                    - Main Menu
                        1. Show Doctor Details
                         2. Show Staff Details
                         3. Add New Doctor
                            - Doctor Name
                            - Doctor ID
                            - Experience
                            - Speciality
                            - Status
                                - Active
                                - Waiting (Initially)
                            - Doctor Password
                         4. Add New Staff
                            - Staff Name
                            - Staff Email
                            - Staff Password
                            - Age
                         5. Exit Management System
                            - Redirect to Main Application Page
    2. Logout/Exit from Management System
        - Redirect to Main Application Page

2. Doctor Module
    - PreDefine Registration values
        - UserName
        - Password
    1. Login to Doctor System
        - Login with UserName and Password
        - Show Welcome to Doctor Home Page Message
        - Login Doctor
                - Successfully Login to Doctor Account
                - Welcome to <Doctor Name> Message
                - After Login Show Main Menu
                    - Main Menu
                        1. Active Status
                            1. Activate
                                - If selected activate (Show Successfully Activated)
                                - Redirect to Login Page
                            2. Waiting
                                - If selected Waiting (Show Waiting Updated)
                                - Redirect to Login Page
                        2. Patient Appointments
                            1. Show Patient Details
                            2. Accept/Reject Patient Appointment
                                - If accepted (Show Accepted)
                                    - Show Patient Details
                                    - Active/Waiting Status
                                - If rejected (Show Rejected)
                                    - Show Patient Details
                                    - Login Menu
                        3. Exit Doctor System
                            - Redirect to Main Application Page

3. Staff Module
    - PreDefine Registration values
        - UserName
        - Password
    1. Login to Staff System
        - Login with UserName and Password
        - Show Welcome to Staff Home Page Message
        - Login Staff
                - Successfully Login to Staff Account
                - Welcome to <Staff Name> Message
                - After Login Show Main Menu
                    - Main Menu
                        1. Patient Appointments List
                            -Show
                                - Patient Name
                                - Doctor Acceptance Status
                            - Enter Patient Name
                            - Enter Doctor ID
                            - Enter Disease
                            - Enter Status
                        - Display Successfully Sent Details to Doctor
                        2. Doctor List
                            - Doctor List with Status
                        3. Patient Report Update
                            - Enter Patient Name
                            - Report Update (Solved/Not Solved)
                        4. Exit Staff System
                            - Redirect to Main Application Page

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
        print("#-#-#-#-#---- Welcome to Application based Hospital Management System ----#-#-#-#-#")
        print("1. Management")
        print("2. Doctor")
        print("3. Staff")
        print("4. Patient")
        c = self.choice()
        if c == 1:
            import Mngmt
            Mngmt.m.login()
        elif c == 2:
            import Dt
            Dt.d.login()
        elif c == 3:
            import Stf
            Stf.s.login()
        elif c == 4:
            import Ptnt
            Ptnt.p.login()
        else:
            print("Invalid choice. Exiting...")

m = main()
m.main()
