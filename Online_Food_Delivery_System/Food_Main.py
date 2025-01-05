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
        print("\n******---- Welcome to Food Delivery System ----******")
        print("1. Food Delivery Admin")
        print("2. Food Delivery Partner")
        print("3. Customer")
        print("4. Exit")
        c = self.choice()
        if c == 1:
            import Food_Admin
            Food_Admin.fa.fa_login()
        elif c == 2:
            import Food_Partner
            Food_Partner.fp_choice()
        elif c == 3:
            import Food_Customer
            Food_Customer.fc_choice()
        elif c == 4:
            exit()
        else:
            print("Invalid choice. Exiting...")

fm = main()
fm.main()


