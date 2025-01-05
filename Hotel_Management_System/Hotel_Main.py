'''
login -> room list with numbers and price -> show date and time when booked room and show exit time limit -> do payment complete when booking
room -> vacates room -> details goes to staff, admin -> admin changes room status from occupied to open
'''

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

class main:
    def main(self):
        print("\n!-------( Welcome to Hotel Management System )-------!")
        print("1. Hotel Admin Management")
        print("2. Hotel Staff")
        print("3. Hotel Customers")
        print("4. Exit")
        c = choice()
        if c == 1:
            import Hotel_Management_Admin
            Hotel_Management_Admin.ha.a_login()
        elif c == 2:
            import Hotel_Staff
            Hotel_Staff.hs.soptions()
        elif c == 3:
            import Hotel_Customer
            Hotel_Customer.hc_choice()
        elif c == 4:
            exit()
        else:
            print("Invalid choice. Exiting...")

hm = main()
hm.main()