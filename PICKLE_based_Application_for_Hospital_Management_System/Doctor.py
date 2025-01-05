from Management import *
from Patient import *
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

class doctor:
    def d_login(self,dUn):
        print("\n<------ Doctor Login Menu ------>")
        dU = get_non_empty_input("Enter Doctor UserName: ")
        pas = get_non_empty_input("Enter Doctor Password: ")
        dUn = dU
        with open("doctor.pkl", "rb") as f:
            try:
                while True:
                    dd = pickle.load(f)
                    if dd._doctor_info__docname == dU and dd._doctor_info__docpassword == pas:
                        self.doctor_menu(dUn,dId=dd._doctor_info__docid)
                        return
                    else:
                        continue
            except EOFError:
                print("Doctor Username not found.")
                self.d_login(dUn)

    def change_stat(self, id, stat):
        docs = []
        updated = False
        with open("doctor.pkl", "rb") as f:
            try:
                while True:
                    dd = pickle.load(f)
                    if dd._doctor_info__docid == id:
                        dd._doctor_info__docstat = stat
                        updated = True
                    docs.append(dd)
            except EOFError:
                if not updated:
                    print("Doctor ID not found.")
                    return
        with open("doctor.pkl", "wb") as f:
            for dd in docs:
                pickle.dump(dd, f)

        print(f"Status has been successfully updated for doctor ID {id}.")

    def pat_stat(self, Pname, Pstat, dId):
        pats = []
        updated = False
        with open("patient.pkl", "rb") as f:
            try:
                while True:
                    pp = pickle.load(f)
                    if pp._patient_info__Pname == Pname:
                        pp._patient_info__Pstat = Pstat
                        pp._patient_info__doctor_id = dId
                        updated = True
                    pats.append(pp)
            except EOFError:
                if not updated:
                    print("Patient Name not found.")
                    return
        with open("patient.pkl", "wb") as f:
            for pp in pats:
                pickle.dump(pp, f)

        print(f"Status has been successfully updated for patient {Pname}.")

    def doctor_menu(self, dUn,dId):
        print("\n\t\t\t<------ Doctor Menu ------>")
        # with open("doctor.pkl", "rb") as f:
            # dd = pickle.load(f)
        print(f"<---------- Welcome to Dr.{dUn}'s Home Page ---------->")
        print("1. Update Status")
        print("2. Patient Appointments")
        print("3. Exit Doctor System")
        c = choice()
        if c == 1:
            did = int(input("Enter Doctor ID: "))
            print("1. Activate")
            print("2. Waiting")
            while True:
                ss = choice()
                if ss == 1:
                    self.change_stat(did, "Active")
                    print(f"Doctor {did} is now Active.")
                    break
                elif ss == 2:
                    self.change_stat(did, "Waiting")
                    print(f"Doctor {did} is now Waiting.")
                    break
            self.doctor_menu(dUn,dId)

        elif c == 2:
            print("\n--- Current List of Patients: ---")
            try:
                with open("patient.pkl", "rb") as f:
                    pats = pickle.load(f)
                    print(
                        f"Patient Name: {pats._patient_info__Pname} \nProblem: {pats._patient_info__prob} \nMobile Number: {pats._patient_info__Pmobile} \nStatus: {pats._patient_info__Pstat} \nDoctor ID: {pats._patient_info__doctor_id}")
            except EOFError:
                pass
            else:
                print("-" * 30)
                print("1. Accept/Reject Patient Appointment")
                print("2. Go Back to Main Menu")
                action = choice()
                if action == 1:
                    while True:
                        Pname = get_non_empty_input("Enter Patient Name: ")
                        with open("patient.pkl", "rb") as f:
                            try:
                                while True:
                                    pp = pickle.load(f)
                                    if pp._patient_info__Pname == Pname:
                                        print("1. Accept")
                                        print("2. Reject")
                                        ss = choice()
                                        if ss == 1:
                                            self.pat_stat(Pname, "Active", dId)
                                            print(f"Patient {Pname} is now Active.")
                                            break
                                        elif ss == 2:
                                            self.pat_stat(Pname, "Waiting", dId)
                                            print(f"Patient {Pname} is now Waiting.")
                                            break
                            except EOFError:
                                print(f"Patient Name {Pname} not found. Please try again.")
                                continue
                        self.doctor_menu(dUn,dId)
                elif action == 2:
                    self.doctor_menu(dUn,dId)
                else:
                    print("Invalid choice. Returning to Main Menu.")
                    self.doctor_menu(dUn,dId)
        elif c == 3:
            print("\n<------ Exiting Doctor System ------>")
            import Main
            Main.main()
        else:
            print("Invalid choice. Please try again.")
            self.doctor_menu(dUn,dId)




d = doctor()
d.d_login(dUn=None)