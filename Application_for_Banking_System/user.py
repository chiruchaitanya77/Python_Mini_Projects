class usr:

    def __init__(self):
        self.__Uname = None
        self.__Upassword = None
        self.__Uaccount = None
        self.__UStatus = None
        self.__balance = None

    def set_name(self,Uname):
        self.__Uname = Uname
        return

    def get_name(self):
        return self.__Uname

    def set_password(self,Upassword):
        self.__Upassword = Upassword
        return

    def get_password(self):
        return self.__Upassword

    def set_account(self,Uaccount):
        self.__Uaccount = Uaccount
        return

    def get_account(self):
        return self.__Uaccount

    def set_status(self,Ustatus):
        self.__Ustatus = Ustatus
        return

    def get_status(self):
        return self.__Ustatus

    def set_balance(self,balance):
        self.__balance = balance
        return

    def get_balance(self):
        return self.__balance

    def get_user_list(self):
        return (f'User Name: {u.get_name()}\nUser Password: {u.get_password()} \nUser Account: {u.get_account()} \nUser Status: {u.get_status()} \nUser Balance: {u.get_balance()}')

def choice(choice=None):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class reg():
    Ulist = []

    def register(self):
        print("<--------! User Register page !-------->")
        new_user = usr()
        new_user.set_name(input("Enter Name: "))
        new_user.set_password(input("Enter Password: "))
        while True:
            try:
                new_user.set_account(int(input("Enter Account Number: ")))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        new_user.set_status("Deactivated")
        new_user.set_balance(0)
        self.Ulist.append(new_user)
        print("<--------! User Register Successful !-------->")
        for user in self.Ulist:
            print(
                f'User Name: {user.get_name()}\nUser Password: {user.get_password()} \nUser Account: {user.get_account()} \nUser Status: {user.get_status()} \nUser Balance: {user.get_balance()}')
        r.options()

    # Down is Buggy code that updates existing values with new values and stores redundant values (Here to know the mistakes)
    # def register(self):
    #     # if r.Ulist:
    #     #     print("DataBase is Working!")
    #     #     r.u_login()
    #     # else:
    #     print("<--------! User Register page !-------->")
    #     u.set_name(input("Enter Name: "))
    #     u.set_password(input("Enter Password: "))
    #     while True:
    #         try:
    #             u.set_account(int(input("Enter Account Number: ")))
    #             break
    #         except ValueError:
    #             print("Invalid input. Please enter a valid number.")
    #     u.set_status("Deactivated")
    #     u.set_balance(0)
    #     self.Ulist.append(u)
    #     print("<--------! User Register Successful !-------->")
    #     for _ in reg.Ulist:
    #         print(f'User Name: {u.get_name()}\nUser Password: {u.get_password()} \nUser Account: {u.get_account()} \nUser Status: {u.get_status()} \nUser Balance: {u.get_balance()}')
    #     r.options()

    def options(self):
        print("<--------- User Options page -------->")
        print("1. Register User")
        print("2. Login User")
        c = choice()
        if c == 1:
            print("<--------- Register for another user -------->")
            self.register()
        if c == 2:
            self.u_login()

    def u_login(self):
        print("<--------! User Login page !-------->")
        uN = input("Enter User Name: ")
        uP = input("Enter User Password: ")
        for i in self.Ulist:
            if i.get_name() == uN and i.get_password() == uP:
                print("<@@@@@@ Login Successful @@@@@@>")
                if i.get_status() == "Deactivated":
                    print("***** WARNING *****\nYour account is deactivated. Please contact manager for further details.")
                    import mn
                    mn.m.main()
                else:
                    r.start()
            else:
                print("Invalid login credentials")
                r.u_login()

    def validate_account(self, acc):
        if acc == u.get_account():
            print("Account number is valid")
            r.operations(acc)
        else:
            print("Account number does not match our records! Please try again.")

    def start(self):
        while True:
            try:
                acc = int(input("\nTo Confirm Please Enter your Account number : "))
                r.validate_account(acc)
            except ValueError:
                print("Invalid input. Please enter a valid account number.")

    def operations(self, acc):
        while True:
            print("\nHere are the User Operations available :")
            print("1. Balance Enquiry")
            print("2. WithDraw")
            print("3. Deposits")
            print("4. Exit Banking System")
            try:
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    print(r.enquiry(acc))
                elif choice == 2:
                    amount = int(input("Enter the amount to be withdrawn : "))
                    r.withdraw(acc, amount)
                elif choice == 3:
                    amount = int(input("Enter the amount to be deposited : "))
                    r.deposit(acc, amount)
                elif choice == 4:
                    import mn
                    mn.m.main()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def deposit(self, acc, amount):
        if acc == u.get_account():
            u.set_balance(u.get_balance() + amount)
            print("Deposit Successful")
            print(f"Account number of {acc} with your new balance : {u.get_balance()}")
            r.operations(acc)
        else:
            print("Invalid Account!")
            r.deposit(acc, amount)

    def enquiry(self, acc):
        if acc == u.get_account():
            return f"Your Bank Balance is: {u.get_balance()}"
        else:
            return "Invalid Account!"

    def withdraw(self, acc, amount):
        if acc == u.get_account():
            if amount > u.get_balance():
                print("Insufficient Balance")
            else:
                u.set_balance(u.get_balance() - amount)
                print("Withdrawal Successful")
                print(f"Your Bank Balance is: {u.get_balance()}")
        else:
            print("Invalid Account!")
        return 0

u = usr()
r = reg()
