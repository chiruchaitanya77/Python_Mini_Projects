import os
import pickle

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

class patient_info:
    def __init__(self, __Pname, __prob, __Pmobile, __Pstat, __doctor_id):
        self.__Pname = __Pname
        self.__prob = __prob
        self.__Pmobile = __Pmobile
        self.__Pstat = __Pstat
        self.__doctor_id = __doctor_id
    def set_Pname(self, __Pname):
        self.__Pname = __Pname
    def get_Pname(self):
        return self.__Pname
    def set_prob(self, __prob):
        self.__prob = __prob
    def get_prob(self):
        return self.__prob
    def set_Pmobile(self, __Pmobile):
        self.__Pmobile = __Pmobile
    def get_Pmobile(self):
        return self.__Pmobile
    def set_Pstat(self, __Pstat):
        self.__Pstat = __Pstat
    def get_Pstat(self):
        return self.__Pstat
    def set_doctor_id(self, __doctor_id):
        self.__doctor_id = __doctor_id
    def get_doctor_id(self):
        return self.__doctor_id

class Patient:
    def login(self):
        print("\n<----------Patient Login Page---------->")
        p.uN = get_non_empty_input("Enter Patient UserName: ")
        p.Pd = get_non_empty_input("Enter Patient Password: ")
        if p.uN == "p" and p.Pd == "p":
            print("Successfully Login Patient Account \n")
            p.patient_menu()
        else:
            print("Invalid login credentials. Please try again")
            p.login()

    def book_app(self, Pname, prob, Pmobile, Pstat, doctor_id):
        p = patient_info(Pname, prob, Pmobile, Pstat, doctor_id)
        if os.path.exists("patient.pkl"):
            with open("patient.pkl", "rb") as f:
                try:
                    pats = pickle.load(f)  # Load existing list of doctors
                except EOFError:
                    pass
        # else:
        with open("patient.pkl", "ab+") as f:
            pickle.dump(p, f)


    def patient_menu(self):
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
                while True:
                    try:
                        Pmobile = int(input("Enter your Mobile Number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue
                print("\n-------( Show Successfully Booked Appointment Details )-------")
                self.book_app(Pname, prob, Pmobile, Pstat, doctor_id)
                try:
                    with open("patient.pkl", "rb") as f:
                        pats = pickle.load(f)
                        print(f"Patient Name: {pats._patient_info__Pname} \nProblem: {pats._patient_info__prob} \nMobile Number: {pats._patient_info__Pmobile} \nStatus: {pats._patient_info__Pstat} \nDoctor ID: {pats._patient_info__doctor_id}")
                except EOFError:
                    pass
                p.patient_menu()


        if c == 2:
            pass
        if c == 3:
            print("\n<------ Exiting Patient System ------>")
            import Main
            Main.main()



p = Patient()
# p.login()