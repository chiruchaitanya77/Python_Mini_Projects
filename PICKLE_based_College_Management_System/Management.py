import pickle

class teacher_info:
    def __init__(self, __username, __password, __id):
        self.__username=__username
        self.__password=__password
        self.__id=__id

    def set_username(self, __username):
        self.__username=__username
    def get_username(self):
        return self.__username
    def set_password(self, __password):
        self.__password=__password
    def get_password(self):
        return self.__password
    def set_id(self, __id):
        self.__id=__id
    def get_id(self):
        return self.__id
    def get_teacher_info(self):
        return (f'User Name: {self.get_username()}\nPassword: {self.get_password()}\nID: {self.get_id()}')

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

class management():
    def __init__(self):

        self.mdata = {1:"m1", 2:"m2", 3:"m3"}
        self.tsdata = {}

    def m_login(self):
        print("\n<------ Management Login Menu ------>")
        while True:
            try:
                id = int(input("Please enter Manager Login id: "))
                break
            except:
                print("Invalid input. Please valid number.")
                continue
        name = input("Please enter Manager Login name: ")
        for key, value in self.mdata.items():
            print(f"{key}: {value}")
            if id in self.mdata and name == self.mdata[id]:
                print('Welcome ' + self.mdata[id])
                m.management_menu()
                return
            else:
                print("Wrong ID or name. Please try again.")

    def add_teacher(self, username, password, id):
        t = teacher_info(username, password, id)
        with open("teachers.pickle", "ab+") as f:
            pickle.dump(t, f)

    # def remove_teacher(self, __username):
    #     uN = input("Enter Teacher Name: ")
    #     with open("teachers.pickle", "rb") as f:
    #         data = pickle.load(f)
    #         data = [entry for entry in data if entry["username"] != uN]
    #     print("Updated data saved successfully!")
    #     print(data)
    #     with open("teachers.pickle", 'wb') as f:
    #         pickle.dump(data, f)
    #     print("Updated data saved successfully!")

    def management_menu(self):
        while True:
            print("\n<------ Management Menu ------>")
            print("1. Add Teacher")
            print("2. Show Teacher Details")
            print("3. Exit")
            c = choice()
            if c == 1:
                self.teacher_register()
                break
            elif c == 2:
                with open("teachers.pickle", "rb") as f:
                    while True:
                        try:
                            data = pickle.load(f)
                            print("ID: ", data._teacher_info__id)
                            print("Username: ", data._teacher_info__username)
                            print("Password: ", data._teacher_info__password)
                        except EOFError:
                            break
            elif c == 3:
                import main
                main.m.main_menu()
                break
            else:
                print("Invalid choice. Please enter a valid number.")

    def teacher_register(self):
        import os
        while True:
            uNt = input("Enter Teacher Name or d to quit: ")
            if uNt == "d":
                break
            else:
                with open("teachers.pickle", "rb+") as f:
                    if os.path.getsize("teachers.pickle") == 0:
                        break
                    else:
                        data = pickle.load(f)
                        if data._teacher_info__username == uNt:
                            print("UserName already exists. Please choose different Username.")
                        else:
                            break
        while True:
            uPw = input("Enter Teacher Password: ")
            if uPw == "d":
                break
            else:
                with open("teachers.pickle", "rb+") as f:
                    if os.path.getsize("teachers.pickle") == 0:
                        break
                    else:
                        data = pickle.load(f)
                        if data._teacher_info__password == uPw:
                            print("Password already exists. Please choose different Password.")
                        else:
                            break
        while True:
            uId = int(input("Enter Teacher ID: "))
            if uId == "d":
                break
            else:
                with open("teachers.pickle", "rb+") as f:
                    if os.path.getsize("teachers.pickle") == 0:
                        break
                    else:
                        data = pickle.load(f)
                        if data._teacher_info__id == uId:
                            print("ID already exists. Please choose different ID.")
                            continue
                        else:
                            break

        self.add_teacher(uNt, uPw, uId)
        print("Teacher added successfully!")

        with open("teachers.pickle", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    print("ID: ", data._teacher_info__id)
                    print("Username: ", data._teacher_info__username)
                    print("Password: ", data._teacher_info__password)
                except EOFError:
                    break

m = management()