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
        print("\n#-#-#-#-#---- Welcome to 4. Book Shop ----#-#-#-#-#")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        c = self.choice()
        if c == 1:
            import Admin
            Admin.a.man_login()
        elif c == 2:
            import Customer
            Customer.us_choice()
        elif c == 3:
            exit()
        else:
            print("Invalid choice. Exiting...")

m = main()
m.main()


