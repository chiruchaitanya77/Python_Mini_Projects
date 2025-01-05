'''
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
'''

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

class management:
    def __init__(self):
        self.Cusername = "m"
        self.Cpassword = "mj"
        self.doctor = {1: ['d1', 'dp1', 'Exp1', 'Sp1', 'Waiting'], 2: ['d2', 'dp2', 'Exp2', 'Sp2', 'Active']}
        self.staff = {'st1':['se1', 'sp', '20'], 'st2':['se2', 'sp', '25']}

    def login(self):
        print("\n<----------Management Login Page---------->")
        self.uN = get_non_empty_input("Enter Management UserName: ")
        self.Pd = get_non_empty_input("Enter Management Password: ")
        if self.uN == m.Cusername and self.Pd == m.Cpassword:
            print("Successfully Login Company Account \n")
            m.management_menu()
        else:
            print("Invalid login credentials. Please try again")
            m.login()

    def management_menu(self):
        print("****----> Welcome to Management System <----****")
        print("1. Show Doctor Details")
        print("2. Show Staff Details")
        print("3. Add New Doctor")
        print("4. Add New Staff")
        print("5. Exit Management System")
        c = choice()
        if c == 1:
            print("\n****----> Doctor Details <----****")
            for d_id, details in m.doctor.items():
                print(f"ID: {d_id} \nName: {details[0]} \nPassword: {details[1]} \nExperience: {details[2]} \nSpeciality: {details[3]} \nStatus: {details[4]}")
            m.management_menu()
        elif c == 2:
            print("\n****----> Staff Details <----****")
            for staff_name, details in m.staff.items():
                print(f"Name: {staff_name}, ID: {details['id']}")
            m.management_menu()
        elif c == 3:
            print("\n****----> Add New Doctor <----****")
            m.doctor_add()
        elif c == 4:
            print("\n****----> Add New Staff <----****")
            m.staff_add()
        elif c == 5:
            print("\n****----> Exiting Management System <----****")
            __import__("com").main_menu()

    def doctor_add(self):
        if not hasattr(self, "doctor"):
            self.doctor = {}
        while True:
            doc_name = get_non_empty_input("Enter the name of the doctor or type 'done' to finish: ")
            if doc_name.lower() == "done":
                self.management_menu()
                return
            doc_id = get_non_empty_input("Enter the ID of the doctor: ")
            try:
                doc_id = int(doc_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
                continue
            if doc_id in self.doctor:
                print("ID already exists. Please try again with a unique ID.")
                continue
            doc_pd = get_non_empty_input("Enter doctor password: ")
            while True:
                try:
                    experience = int(input("Enter the experience of the doctor: "))
                except ValueError:
                    print("Invalid experience. Please enter a numeric value.")
                    continue
            speciality = get_non_empty_input("Enter the speciality of the doctor: ")
            status = None
            while True:
                print("Set Status:")
                print("1. Active\n2. Waiting")
                try:
                    c = int(choice())
                    if c == 1:
                        status = "Active"
                        print(f"Status for {doc_name} set to Active")
                        break
                    elif c == 2:
                        status = "Waiting"
                        print(f"Status for {doc_name} set to Waiting")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid choice. Please enter a valid number (1 or 2).")

            self.doctor[doc_id] = [doc_name, doc_pd, experience, speciality, status]
            print(f"\nDoctor '{doc_name}' has been successfully added!")

            print("\nCurrent List of Doctors:")
            for d_id, details in self.doctor.items():
                print(f"Doctor ID: {d_id}")
                print(f"Doctor Name: {details[0]}")
                # print(f"Doctor Password: {details[1]}")
                print(f"Experience: {details[2]}")
                print(f"Speciality: {details[3]}")
                print(f"Status: {details[4]}")
                print("-" * 30)
        m.management_menu()

    def staff_add(self):
        if not hasattr(self, "staff"):
            self.staff = {}
        while True:
            st_name = get_non_empty_input("Enter the name of the Staff or type 'done' to finish: ")
            if st_name.lower() == "done":
                self.management_menu()
                return
            if st_name in self.staff:
                print("Name already exists. Please try again with a unique Name.")
                continue
            st_em = get_non_empty_input("Enter staff Email: ")
            st_pd = get_non_empty_input("Enter staff password: ")
            st_ag = get_non_empty_input("Enter the age of staff: ")

            self.staff[st_name] = [st_em, st_pd, st_ag]
            print(f"\nStaff '{st_name}' has been successfully added!")

            print("\nCurrent List of Staff:")
            for st_name, details in self.staff.items():
                print(f"Staff Name: {st_name}")
                print(f"Staff Email: {details[0]}")
                print(f"Staff Password : {details[1]}")
                print(f"Age: {details[2]}")
                print("-" * 30)

    def get_doc_ids(self):
        for d_id, details in m.doctor.items():
            return (f"ID: {d_id} \nName: {details[0]} \nPassword: {details[1]} \nExperience: {details[2]} \nSpeciality: {details[3]} \nStatus: {details[4]}")
    def get_staff_ids(self):
        for st_name, details in m.staff.items():
            return (f"Name: {st_name}, Staff Email: {details[0]}, Staff Password : {details[1]}, Age: {details[2]}")
m = management()