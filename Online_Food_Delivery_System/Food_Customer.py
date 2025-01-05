import datetime

class fc:
    def __init__(self):
        self.FCusername = None
        self.__FCname = None
        self.__FCpassword = None
        self.__FCnumber = None
        self.FCaddress = None

    def set_username(self,FCusername):
        self.__FCusername = FCusername
        return

    def get_username(self):
        return self.__FCusername

    def set_name(self,FCname):
        self.__FCname = FCname
        return

    def get_name(self):
        return self.__FCname

    def set_password(self,FCpassword):
        self.__FCpassword = FCpassword
        return

    def get_password(self):
        return self.__FCpassword

    def set_number(self,FCnumber):
        self.__FCnumber = FCnumber
        return

    def get_number(self):
        return self.__FCnumber

    def get_customer_list(self):
        return (f'User Name: {f.get_username()}\nName: {f.get_name()}\nUser Password: {f.get_password()}\nPhone Number: {f.get_number()}')

def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def fc_choice():
    while True:
        print("<------ Customer Menu ------>")
        print("1. Register")
        print("2. Login")
        print("3. Exit Customer")
        try:
            c = choice()
            if c == 1:
                fcc.fcregister()
            if c == 2:
                fcc.fc_login()
            if c == 3:
                import Food_Main
                Food_Main.fm.main()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class food_customer():
    FClist = []
    Flist = ([["Dish1", 100], ["Dish2", 150], ["Dish3", 200], ["Dish4", 250]],
             [["Dish5", 300], ["Dish6", 350], ["Dish7", 400], ["Dish8", 450]],
             [["Dish9", 500], ["Dish10", 550], ["Dish11", 600], ["Dish12", 650]],
             [["Dish13", 700], ["Dish14", 750], ["Dish15", 800], ["Dish16", 850]])
    Hlist = ["Hotel1", "Hotel2", "Hotel3", "Hotel4"]
    COlist = []
    def fcregister(self):
        print("<--------! User Register page !-------->")
        new_user = fc()
        while True:
            username = input("Enter User Name: ")
            if any(user.get_username() == username for user in self.FClist):
                print("UserName already exists. Please enter a different username.")
                continue
            else:
                new_user.set_username(username)
                break
        while True:
            name = input("Enter Name: ")
            if any(user.get_name() == name for user in self.FClist):
                print("Name already exists. Please enter a different name.")
                continue
            else:
                new_user.set_name(name)
                break
        while True:
            try:
                number = int(input("Enter Phone Number: "))
                if len(str(number)) != 10:
                    print("Invalid phone number. Please enter a valid 10-digit phone number.")
                    continue
                if any(user.get_number() == number for user in self.FClist):
                    print("Phone number already exists. Please enter a different phone number.")
                    continue
                else:
                    new_user.set_number(number)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        while True:
            password = input("Enter Password: ")
            if any(user.get_password() == password for user in self.FClist):
                print("Password too similar to an existing customer. Please enter a unique password.")
                continue
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue
            else:
                new_user.set_password(password)
                break
        self.FClist.append(new_user)
        print("<--------! User Register Successful !-------->")
        for user in self.FClist:
            print(f'User Name: {user.get_username()}\nName: {user.get_name()}\nUser Password: {user.get_password()}\nPhone Number: {user.get_number()}')
        fc_choice()

    def fc_login(self):
        print("<--------! User Login page !-------->")
        uN = input("Enter User Name: ")
        uP = input("Enter User Password: ")
        found_user = next((user for user in self.FClist if user.get_username() == uN and user.get_password() == uP), None)
        if found_user:
            print("<@@@@@@ Login Successful @@@@@@>")
            self.fcoperations(found_user)
        else:
            print("Invalid login credentials")
            self.fc_login()

    def fcoperations(self, logged_in_customer):
        while True:
            print("\n<-------! Customer Main Menu Page !------->")
            print("1. View/Order Food")
            print("2. View Order History")
            print("3. Exit Customer Menu")
            c = choice()
            if c == 1:
                while True:
                    print("\n<-------------! View Food Page !---------------->")
                    print("\n<-------------! AVAILABLE DISHES !-------------->")
                    for rv, r in zip(fcc.Hlist, fcc.Flist):
                        print(f"|\t\t\t\tHotel: {rv}\t\t\t\t\t|\n|\t\tDish Name/Price: {r[0]}  \t\t|\n|\t\tDish Name/Price: {r[1]}  \t\t|\n|\t\tDish Name/Price: {r[2]}  \t\t|\n|\t\tDish Name/Price: {r[3]} \t\t|")
                        print('-' * 49)
                    break
                while True:
                    print("\n<--------- Food Ordering Page !-------->")
                    print("1. Order Food ")
                    print("2. Back to Menu")
                    c = choice()
                    if c == 1:
                        hN = int(input("Enter the Hotel Number: "))
                        if 0 <= hN < len(fcc.Hlist):
                            print('-' * 57)
                            print(f"\t\t\t\tHotel Details: {fcc.Hlist[hN-1]}")
                            print('-' * 57)
                            for i in range(len(fcc.Flist[hN])):
                                print(f"Dish Number: {i+1} \t\tDish Name: {fcc.Flist[hN-1][i][0]} \t\tPrice: Rs.{fcc.Flist[hN-1][i][1]}")
                        print('-' * 57)
                        fN = int(input("Enter the Dish Number: "))
                        if 0<= fN < len(fcc.Flist[hN]):
                            print(f"Dish Details: {fcc.Flist[hN-1][fN-1][0]} \t\tPrice: Rs.{fcc.Flist[hN-1][fN-1][1]}")
                            print('-' * 57)
                        pay = input("Do you want to pay now? (Y/N) : ")
                        while True:
                            if pay.lower() == "y":
                                pay_amount = int(input(f"Enter Payment Amount of Rs.{fcc.Flist[hN-1][fN-1][1]}: "))
                                if pay_amount == fcc.Flist[hN-1][fN-1][1]:
                                    print("Payment Successful ✅")
                                    order_id = len(fcc.COlist) + 1
                                    delivery_status = "Not Delivered"
                                    customer_issues = input("Do you have any customer issues? Mention them : ")
                                    fcc.COlist.append((order_id, logged_in_customer, hN, fN, pay_amount, delivery_status, customer_issues))
                                    current_time = datetime.datetime.now().time().strftime("%I:%M %p")
                                    print(f'Order "{order_id}" for "{fcc.Flist[hN-1][fN-1][0]}" placed successfully by "{logged_in_customer.get_username()}" on {current_time}')
                                    self.fcoperations(logged_in_customer)
                                else:
                                    print(f"Payment Failed. Required amount is Rs.{fcc.Flist[hN-1][fN-1][1]}")
                                    continue
                            elif pay.lower() == "n":
                                print("Payment Cancelled ... Returning to Main Menu.")
                                self.fcoperations(logged_in_customer)
                    if c == 2:
                        self.fcoperations(logged_in_customer)
            if c == 2:
                self.fc_order_history(logged_in_customer)

            if c == 3:
                import Food_Main
                Food_Main.fm.main()
                
    def fc_order_history(self, logged_in_customer):
        print("<------ Order History ------>")
        user_orders = [order for order in self.COlist if order[1] == logged_in_customer]
        if not user_orders:
            print("No Orders Found!")
        else:
            print("-" * 40)
            for order in user_orders:
                order_id, _, hotel, dish, amount, delivery_status, issues = order
                print(f"Order ID: {order_id}")
                print(f"Hotel: {self.Hlist[hotel - 1]}")
                print(f"Dish: {self.Flist[hotel - 1][dish - 1][0]}")
                print(f"Price: Rs.{amount}")
                print(f"Delivery Status: {delivery_status}")
                print(f"Customer Issues: {issues if issues else 'None'}")
            print("-" * 40)

    def issue(self, order_id, logged_in_customer):
        pass
                    

fcc = food_customer()
f = fc()