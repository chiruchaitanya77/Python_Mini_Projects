def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

from Food_Customer import fcc

class admin:
    def __init__(self):
        self.name = "a"
        self.password = "1"

    def fa_login(self):
        print("<------ Food Admin Login page ------>")
        mN = input("Enter admin name: ")
        mP = input("Enter admin password: ")
        if mN == self.name and mP == self.password:
            print("Admin Login Successful")
            fa.fa_menu()
        else:
            print("Invalid login credentials")
            fa.fa_login()

    def fa_menu(self):
        print("<------ Food Admin menu ------>")
        while True:
            print("1. View Delivery Details")
            print("2. View Issues")
            print("3. Exit Admin System")
            c = choice()
            if c == 1:
                print("\nOrders Details:")
                print('-' * 30)
                if len(fcc.COlist) != 0:
                    for order in fcc.COlist:
                        if order[5] == "Delivered":
                            print(f"Order ID: {order[0]}\nDelivery Status: {order[5]}\nHotel Number: {order[2]}\nDish Number: {order[3]}\nCustomer: {order[1].get_username()}\nAmount Paid: {order[4]}")
                    print('-' * 30)
                else:
                    print("NO orders Found!")
                    print('-' * 30, "\n")
            if c == 2:
                print('-' * 30)
                print("Not resolved Customer Issues:")
                print('-' * 30)
                if len(fcc.COlist) != 0:
                    for order in fcc.COlist:
                        if order[5] == "Delivered" and order[6] != "None":
                            print(f"Order ID: {order[0]}\nCustomer: {order[1].get_username()}\nCustomer Issue: {order[6]}")
                    print('-' * 30)
                else:
                    print("No Issues from Customers!")
                    print('-' * 30, "\n")
                print("Delivery Partner Issues:")
                print('-' * 30)
                if len(fcc.COlist) != 0:
                    for order in fcc.COlist:
                        if order[5] == "Delivered" and order[6] != "None":
                            print(f"Order ID: {order[0]}\nCustomer: {order[1].get_username()}\nCustomer Issue: {order[6]}\nDelivery Partner Issue: {order[9]}")
                    print('-' * 30)
                else:
                    print("No Issues from Delivery Partners!")
                    print('-' * 30, "\n")
            if c == 3:
                import Food_Main
                Food_Main.fm.main()

fa = admin()