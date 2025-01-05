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

from Teacher import t
from Student import s

class management:
    def __init__(self):

        self.mdata = {1:"m1", 2:"m2", 3:"m3"}
        self.tsdata = {}

    def m_login(self):
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

    def management_menu(self):
        while True:
            print("\nManagement Menu:")
            print("1. Add Teacher")
            print("2. Show Teacher Details")
            print("3. Add Teacher Student")
            print("4. Exit")
            c = choice()
            if c == 1:
                self.t_register()
            elif c == 2:
                for key, value in t.data.items():
                    print("-" * 30)
                    print(f"Teacher name: {value} \nTeacher Id: {key}")
            elif c == 3:
                self.ts_add()
            elif c == 4:
                print(">>>> Exiting Management System >>>>")
                import mn
                mn.m.main_menu()
            else:
                print("Invalid choice. Please enter a valid number.")

    def add_teacher(self, id, name):
        t.data[id] = name

    def add_teacher_student(self, id, name):
        m.tsdata[id] = name

    def t_register(self):
        while True:
            name = input("Enter teacher name or d to quit: ")
            if name.lower() == "d":
                print(">>>> Redirecting to Main menu >>>>")
                m.management_menu()
                return
            try:
                id = int(input("Enter teacher ID: "))
                if id in t.data:
                    print("ID already exists. Please choose different ID.")
                else:
                    self.add_teacher(id, name)
                    print(f"Teacher Account {name} with ID {id} added successfully!\n")
            except ValueError:
                print("Invalid input. Please valid ID.")



    def ts_add(self):
        while True:
            try:
                tid = int(input("Enter Teacher ID: "))
                if tid not in t.data:
                    print("Teacher ID does not exist. Please enter a valid Teacher ID.")
                    continue

                if tid not in self.tsdata:
                    self.tsdata[tid] = []

                name = input("Enter student name or 'd' to quit: ")
                while name.lower() != "d":
                    if name in s.sdata.values():
                        self.tsdata[tid].append(name)
                        print(f"Student {name} added successfully under Teacher ID {tid}!")
                    else:
                        print(f"Student {name} does not exist in the student list (sdata).")
                    name = input("Enter another student name or 'd' to quit: ")
                print("Teacher-Student Data Saved:", self.tsdata)
                print("\n>>>> Redirecting to Main Menu >>>>")
                m.management_menu()
                return
            except ValueError:
                print("Invalid input. Please enter a valid numerical Teacher ID.")


m = management()