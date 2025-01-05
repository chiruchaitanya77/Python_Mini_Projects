from user import r,u

class mngr():
    def __init__(self):
        self.name = "man"
        self.email = "manager@gmail.com"
        self.password = "123123"

    def man_login(self):
        print("Welcome to manager login page")
        mN = input("Enter your manager name: ")
        mP = input("Enter your manager password: ")
        if mN == self.name and mP == self.password:
            print("Manager Login Successful")
            m.man_menu()
        else:
            print("Invalid login credentials")
            m.man_login()

    def man_menu(self):
        print("<------ Manager menu ------>")
        print('<------ User List ------>')
        for user in r.Ulist:
            print(f'User Name: {user.get_name()}\nUser Password: {user.get_password()} \nUser Account: {user.get_account()} \nUser Status: {user.get_status()} \nUser Balance: {user.get_balance()}')

        print("1. Activate Users")
        print("2. Deactivate Users")
        print("3. Exit Manager System")
        c = int(input("Enter your choice: "))
        un = input("Enter username: ")
        for user in r.Ulist:
            if un == user.get_name():
                if c == 1:
                    user.set_status("Active")
                    print(f'{user.get_name()} User Status Updated to {user.get_status()}')
                    m.man_menu()
                if c == 2:
                    user.set_status("Deactivated")
                    print(f'{user.get_name()} User Status Updated to {user.get_status()}')
                    m.man_menu()
                if c == 3:
                    print("<------ Exiting Manager System ------>")
                    import mn
                    mn.m.main()


m = mngr()