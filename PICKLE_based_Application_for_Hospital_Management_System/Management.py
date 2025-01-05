import pickle
import os.path

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

class doctor_info:
    def __init__(self, __docname, __docid, __docpassword, __docexp, __docspec, __docstat):
        self.__docname=__docname
        self.__docid = __docid
        self.__docpassword=__docpassword
        self.__docexp=__docexp
        self.__docspec=__docspec
        self.__docstat=__docstat

    def set_docname(self, __docname):
        self.__docname=__docname
    def get_docname(self):
        return self.__docname
    def set_docid(self, __docid):
        self.__docid=__docid
    def get_docid(self):
        return self.__docid
    def set_docpassword(self, __docpassword):
        self.__docpassword=__docpassword
    def get_docpassword(self):
        return self.__docpassword
    def set_docexp(self, __docexp):
        self.__docexp=__docexp
    def get_docexp(self):
        return self.__docexp
    def set_docspec(self, __docspec):
        self.__docspec=__docspec
    def get_docspec(self):
        return self.__docspec
    def set_docstat(self, __docstat):
        self.__docstat=__docstat
    def get_docstat(self):
        return self.__docstat
    def get_doctor_info(self):
        return self.__docname, self.__docid, self.__docpassword, self.__docexp, self.__docspec, self.__docstat

class staff_info:
    def __init__(self, __stname, __stage, __stemail, __stpassword):
        self.__stname=__stname
        self.__stage=__stage
        self.__stemail=__stemail
        self.__stpassword=__stpassword

    def set_stname(self, __stname):
        self.__stname=__stname
    def get_stname(self):
        return self.__stname
    def set_stage(self, __stage):
        self.__stage=__stage
    def get_stage(self):
        return self.__stage
    def set_stemail(self, __stemail):
        self.__stemail=__stemail
    def get_stemail(self):
        return self.__stemail
    def set_stpassword(self, __stpassword):
        self.__stpassword=__stpassword
    def get_stpassword(self):
        return self.__stpassword
    def get_staff_info(self):
        return self.__stname, self.__stage, self.__stemail, self.__stpassword

class management:
    def __int__(self):
        pass

    def m_login(self):
        Mname = "m"
        Mpassword = "mj"
        print("\n<---------- Management Login Page ---------->")
        uN = get_non_empty_input("Enter Management UserName: ")
        Pd = get_non_empty_input("Enter Management Password: ")
        if uN == Mname and Pd == Mpassword:
            print("Successfully Login Company Account \n")
            m.management_menu()
        else:
            print("Invalid login credentials. Please try again")
            m.m_login()

    def management_menu(self):
        print("****----> Welcome to Management System <----****")
        print("1. Add New Doctor")
        print("2. Show Doctor Details")
        print("3. Add New Staff")
        print("4. Show Staff Details")
        print("5. Exit Management System")
        c = choice()
        if c == 1:
            print("\n****----> Add New Doctor <----****")
            m.doctor_add()
        elif c == 2:
            print("\n****----> Doctor Details <----****")
            with open("doctor.pkl", "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        print("-" * 30)
                        print("Username: ", data._doctor_info__docname)
                        print("ID: ", data._doctor_info__docid)
                        print("Password: ", data._doctor_info__docpassword)
                        print("Experience: ", data._doctor_info__docexp)
                        print("Speciality: ", data._doctor_info__docspec)
                        print("Status: ", data._doctor_info__docstat)
                        print("-" * 30)
                    except EOFError:
                        m.management_menu()
        elif c == 3:
            print("\n****----> Add New Staff <----****")
            m.staff_add()
        elif c == 4:
            print("\n****----> Staff Details <----****")
            with open("staff.pkl", "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        print("-" * 30)
                        print("Username: ", data._staff_info__stname)
                        print("Age: ", data._staff_info__stage)
                        print("Email: ", data._staff_info__stemail)
                        print("Password: ", data._staff_info__stpassword)
                        print("-" * 30)
                    except EOFError:
                        m.management_menu()
        elif c == 5:
            print("\n****----> Exiting Management System <----****")
            import Main
            Main.main()

    def doctor_add(self):
        while True:
            dN = get_non_empty_input("Enter the name of the doctor or type 'd' to finish: ")
            if dN.lower() == "d":
                break
            else:
                doc_name = dN
            doc_id = get_non_empty_input("Enter the ID of the doctor: ")
            try:
                doc_id = int(doc_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
                continue
            doc_pd = get_non_empty_input("Enter doctor password: ")
            while True:
                try:
                    experience = int(input("Enter the experience of the doctor: "))
                    break
                except ValueError:
                    print("Invalid experience. Please enter a numeric value.")
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
                    break
            self.add_doctor(doc_name, doc_id, doc_pd, experience, speciality, status)
            print(f"Doctor {doc_name} added successfully!")

        with open("doctor.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    print("-" * 30)
                    print("Username: ", data._doctor_info__docname)
                    print("ID: ", data._doctor_info__docid)
                    print("Password: ", data._doctor_info__docpassword)
                    print("Experience: ", data._doctor_info__docexp)
                    print("Speciality: ", data._doctor_info__docspec)
                    print("Status: ", data._doctor_info__docstat)
                    print("-" * 30)
                except EOFError:
                    m.management_menu()

    def add_doctor(self, doc_name, doc_id, dec_pd, experience, speciality, status):
        d = doctor_info(doc_name, doc_id, dec_pd, experience, speciality, status)
        if os.path.exists("doctor.pkl"):
            with open("doctor.pkl", "rb") as f:
                try:
                    doctors = pickle.load(f)  # Load existing list of doctors
                except EOFError:
                    pass
        # else:
        with open("doctor.pkl", "ab+") as f:
            pickle.dump(d, f)

    def staff_add(self):
        while True:
            sN = get_non_empty_input("Enter the name of the staff or type 'd' to finish: ")
            if sN.lower() == "d":
                break
            else:
                st_name = sN
            while True:
                try:
                    st_age = int(input("Enter the Age of the staff: "))
                    break
                except ValueError:
                    print("Invalid age. Please enter a numeric value.")
            st_em = get_non_empty_input("Enter staff Email: ")
            st_pd = get_non_empty_input("Enter staff password: ")
        self.add_staff(st_name, st_age, st_em, st_pd)
        print(f"Staff '{st_name}' has been successfully added!")

        with open("staff.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    print("-" * 30)
                    print("Username: ", data._staff_info__stname)
                    print("Age: ", data._staff_info__stage)
                    print("Email: ", data._staff_info__stemail)
                    print("Password: ", data._staff_info__stpassword)
                    print("-" * 30)
                except EOFError:
                    break

    def add_staff(self, st_name, st_age, st_em, st_pd):
        s = staff_info(st_name, st_age, st_em, st_pd)
        if os.path.exists("staff.pkl"):
            with open("staff.pkl", "rb") as f:
                pickle.dump(s, f)
        else:
            with open("staff.pkl", "wb") as f:
                pickle.dump(s, f)





m = management()
# m.m_login()