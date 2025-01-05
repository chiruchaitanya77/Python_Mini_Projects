'''
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
                                - Doctor Acceptance Status (Waiting Initially)
                            - Enter Patient Name
                            - Enter Doctor ID
                            - Enter Disease
                            - Enter Status
                        - Display Details to Doctor
                        2. Doctor List
                            - Doctor List with Status
                        3. Patient Report Update
                            - Enter Patient Name
                            - Report Update (Solved/Not Solved)
                        4. Exit Staff System
                            - Redirect to Main Application Page
'''
from Mngmt import management
manager = management()
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


class Staff:
    def __init__(self):
        self.rep_status = None
        self.p_reports = {}  # Dictionary to store patient names and their report status
        self.uN = None
        self.Pd = None

    def login(self):
        print("<----------Staff Login Page---------->")
        eM = input("Enter Staff Email: ")
        pD = input("Enter Staff Password: ")
        st_ids = manager.get_staff_ids()
        if st_ids:
            if eM in st_ids and pD in st_ids:
                print(f"Successfully Logged into Staff Account \n")
                s.staff_menu()
            else:
                print("Invalid Doctor Id. Please try again.")
                s.login()
        else:
            print("No Staff found in the system.")
            s.login()

    def staff_menu(self):

        global Pname
        print("\n<----------welcome to Staff Main Page---------->")
        print("1. Patient Appointments List")
        print("2. Doctor List")
        print("3. Patient Report Update")
        print("4. Exit Staff System")
        c = choice()
        if c == 1:
            print("\n====== Patient Appointments List =======")
            p_res = pat.p_app.items()
            if p_res:
                patient_names = []
                for Pname, details in p_res:
                    patient_names.append(Pname)
                    print(f"Patient Name: {Pname}")
                    print(f"Problem: {details[0]}")
                    print(f"Mobile Number: {details[1]}")
                    print(f"Status: {details[2]}")
                    print(f"Doctor ID: {details[3]}")
                    print("-" * 30)
                s.staff_menu()

        if c == 2:
            print("\n====== Current List of Doctors ======")
            di = manager.get_doc_ids()
            if di:
                for d_id, details in manager.doctor.items():
                    print(f"Doctor ID: {d_id}")
                    print(f"Doctor Name: {details[0]}")
                    print(f"Doctor Experience: {details[2]}")
                    print(f"Doctor Speciality: {details[3]}")
                    print(f"Doctor Status: {details[4]}")
                    print("-" * 30)
                s.staff_menu()

        if c == 3:
            if not hasattr(self, "p_reports"):
                self.p_reports = {}
            p_res = pat.p_app.items()
            patient_names = []
            if p_res:
                for Pname, details in p_res:
                    patient_names.append(Pname)
            if p_res:
                for Pname, details in p_res:
                    print(f"Patient Name: {Pname}")
            else:
                print("No patient appointments found.")
                return
            p_select = get_non_empty_input("Enter the Patient Name to update the report: ")
            if p_select not in patient_names:
                print(f"Patient {p_select} not found.")
                s.staff_menu()
            print("1. Solved")
            print("2. Not Solved")
            c = choice()
            if c == 1:
                self.rep_status = "Solved"
                print("Report Update Successful")
            elif c == 2:
                self.rep_status = "Not Solved"
                print("Report Update Successful")
            else:
                print("Invalid choice. Please enter a valid number.")
                s.staff_menu()

            self.p_reports[p_select] = self.rep_status
            pn = pat.get_p_app()
            if p_select in pn:
                self.p_reports[p_select] = self.rep_status

                print("\n====== Updated Patient Reports ======")
                print(f"Updated Report: {p_select} -> {self.rep_status}")

                print("\n====== All Patient Reports ======")
                for patient, status in self.p_reports.items():
                    print(f"Patient Name: {patient}, \nReport Status: {status}")
                s.staff_menu()
            else:
                print("\n====== Updated Patient Reports ======")
                print(f"Updated Report: {p_select} -> {self.rep_status}")
                print("\n====== All Patient Reports ======")
                for patient, status in self.p_reports.items():
                    print(f"Patient Name: {patient}, \nReport Status: {status}")
                s.staff_menu()
        if c == 4:
            print("<------ Exiting Staff System ------>")
            from mn import main
            main()


s = Staff()
s.login()