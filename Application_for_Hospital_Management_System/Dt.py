'''
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
'''

from Mngmt import management
manager = management()
from Stf import Staff
staff = Staff()
from Ptnt import Patient
pat = Patient()

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

class Doctor:

    def login(self):
        print("<---------- Doctor Login Page ---------->")
        uN = input("Enter Doctor UserName: ")
        pD = input("Enter Doctor Password: ")

        # Validate if `manager.doctor` has any records
        if not manager.doctor:
            print("No doctors found in the system.")
            self.login()
            return

        # Check if username and password match any doctor in the dictionary
        for doc_id, details in manager.doctor.items():
            if details[0] == uN and details[1] == pD:  # Match both username and password
                print(f"Successfully Logged into Dr.{uN} Account \n")
                self.doctor_menu(doc_id)
                return

        # If no matching doctor found, show error and retry login
        print("Invalid Doctor credentials. Please try again.")
        self.login()

    def doctor_menu(self, doc_id):
        # Ensure the passed `doc_id` exists in `manager.doctor`
        if doc_id not in manager.doctor:
            print("Error: Doctor ID not found. Returning to login.")
            self.login()
            return

        # Display Doctor's Home Page
        print(f"<---------- Welcome to Dr.{manager.doctor[doc_id][0]}'s Home Page ---------->")
        print("1. Update Status")
        print("2. Patient Appointments")
        print("3. Exit Doctor System")
        c = choice()

        # Option 1: Update Status
        if c == 1:
            print("1. Activate")
            print("2. Waiting")
            while True:
                status_choice = choice()
                if status_choice == 1:
                    manager.doctor[doc_id][4] = "Active"
                    print(f"Doctor {doc_id} is now Active.")
                    break
                elif status_choice == 2:
                    manager.doctor[doc_id][4] = "Waiting"
                    print(f"Doctor {doc_id} is now Waiting.")
                    break
                else:
                    print("Invalid choice. Please choose 1 or 2.")
            self.doctor_menu(doc_id)

        # Option 2: Patient Appointments
        elif c == 2:
            print("\n--- Current List of Patients: ---")
            p_res = pat.p_app.items()
            if p_res:
                for Pname, details in p_res:
                    print(f"Patient Name: {Pname}")
                    print(f"Problem: {details[0]}")
                    print(f"Mobile Number: {details[1]}")
                    print(f"Status: {details[2]}")
                    if len(details) > 3:  # Ensure the list has at least 4 elements
                        print(f"Doctor ID: {details[3]}")
                    else:
                        print("Doctor ID: Not Assigned")

                    print("-" * 30)

                print("1. Accept/Reject Patient Appointment")
                print("2. Go Back to Main Menu")
                action = choice()

                if action == 1:
                    # Handle Accept/Reject
                    while True:
                        Pname = get_non_empty_input("Enter Patient Name: ")
                        if Pname in pat.p_app:
                            print("1. Accept")
                            print("2. Reject")
                            decision = choice()
                            if decision == 1:
                                pat.p_app[Pname][2] = "Active"  # Update Patient Status to Active
                                pat.p_app[Pname][3] = doc_id  # Add Doctor ID to Patient Details.
                                print(f"Appointment with Patient {Pname} Accepted and Status updated to Active by Doctor ID: {doc_id}.")
                                self.doctor_menu(doc_id)
                            elif decision == 2:
                                pat.p_app[Pname][2] = "Waiting"  # Update Patient Status to Waiting
                                print(f"Appointment with Patient {Pname} Rejected and Status updated to Waiting.")
                                self.doctor_menu(doc_id)
                            else:
                                print("Invalid choice.")
                            break
                        else:
                            print(f"Patient Name {Pname} not found. Please try again.")
                elif action == 2:
                    self.doctor_menu(doc_id)
                else:
                    print("Invalid choice. Returning to Main Menu.")
                    self.doctor_menu(doc_id)
            else:
                print("No patient appointments found.")
                self.doctor_menu(doc_id)

        # Option 3: Exit Doctor System
        elif c == 3:
            print("\n<------ Exiting Doctor System ------>")
            __import__("mn").main_menu()
        else:
            print("Invalid choice. Please try again.")
            self.doctor_menu(doc_id)


d = Doctor()
