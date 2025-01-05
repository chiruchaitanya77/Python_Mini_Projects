from Customer import r, c

class admin:
    def __init__(self):
        self.name = "a"
        self.email = "admin@gmail.com"
        self.password = "1"

    def man_login(self):
        print("<------ Admin Login page ------>")
        mN = input("Enter your admin name: ")
        mP = input("Enter your admin password: ")
        if mN == self.name and mP == self.password:
            print("Admin Login Successful")
            a.man_menu()
        else:
            print("Invalid login credentials")
            a.man_login()

    def man_menu(self):
        print("<------ Admin menu ------>")
        print('<------ User List ------>')
        for user in r.Clist:
            print(f'User Name: {user.get_name()} \nUser Email: {user.get_email()} \nUser Password: {user.get_password()} \nUser Status: {user.get_status()}')
        print("1. Activate Customer")
        print("2. Deactivate Customer")
        print("3. Show Customers")
        print("4. Show Books")
        print("5. Exit Admin")
        choice = int(input("Enter your choice: "))
        if choice == 3:
            for user in r.Clist:
                print(f'User Name: {user.get_name()} \nUser Email: {user.get_email()} \nUser Password: {user.get_password()} \nUser Status: {user.get_status()}')
        a.man_menu()
        if choice == 4:
            for book in r.Blist:
                print(book)
        a.man_menu()
        if choice == 5:
            print("<------ Exiting Admin ------>")
            import main
            main.m.main()

        for user in r.Clist:
            un = input("Enter Customer name: ")
            if un == user.get_name():
                if choice == 1:
                    user.set_status("Active")
                    print(f'{user.get_name()} User Status Updated to {user.get_status()}')
                    a.man_menu()
                if choice == 2:
                    user.set_status("Deactivated")
                    print(f'{user.get_name()} User Status Updated to {user.get_status()}')
                    a.man_menu()

a = admin()