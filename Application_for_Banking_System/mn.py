class main:
    def choice(choice=None):
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

    def main(self):
        print("\n#-#-#-#-#---- Welcome to Bank Management System v2.0 ----#-#-#-#-#")
        print("1. Manager")
        print("2. User")
        c = self.choice()
        if c == 1:
            import manager
            manager.m.man_login()
        elif c == 2:
            import user
            user.r.register()
        else:
            print("Invalid choice. Exiting...")

m = main()
m.main()


