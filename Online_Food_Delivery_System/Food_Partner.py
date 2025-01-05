from Food_Customer import fcc

class fdp:
    def __init__(self):
        self.FPusername = None
        self.__FPname = None
        self.__FPpassword = None
        self.__FPnumber = None

    def set_username(self,FPusername):
        self.__FPusername = FPusername
        return

    def get_username(self):
        return self.__FPusername

    def set_name(self,FPname):
        self.__FPname = FPname
        return

    def get_name(self):
        return self.__FPname

    def set_password(self,FPpassword):
        self.__FPpassword = FPpassword
        return

    def get_password(self):
        return self.__FPpassword

    def set_number(self,FPnumber):
        self.__FPnumber = FPnumber
        return

    def get_number(self):
        return self.__FPnumber

    def get_partner_list(self):
        return (f'User Name: {f.get_username()}\nName: {f.get_name()}\nUser Password: {f.get_password()}\nPhone Number: {f.get_number()}')

def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def fp_choice():
    while True:
        print("<------ Delivery Partner Menu ------>")
        print("1. Register")
        print("2. Login")
        print("3. Exit Delivery Partner Menu")
        try:
            c = choice()
            if c == 1:
                fp.fpregister()
            if c == 2:
                fp.fp_login()
            if c == 3:
                import Food_Main
                Food_Main.fm.main()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class food_partner():
    FPlist = []
    def fpregister(self):
        print("<--------! Delivery Partner Register page !-------->")
        new_user = fdp()
        while True:
            username = input("Enter User Name: ")
            if any(user.get_username() == username for user in self.FPlist):
                print("UserName already exists. Please enter a different username.")
                continue
            else:
                new_user.set_username(username)
                break
        while True:
            name = input("Enter Name: ")
            if any(user.get_name() == name for user in self.FPlist):
                print("Name already exists. Please enter a different name.")
                continue
            else:
                new_user.set_name(name)
                break
        while True:
            try:
                number = int(input("Enter Phone Number: "))
                if any(user.get_email() == number for user in self.FPlist):
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
            if any(user.get_password() == password for user in self.FPlist):
                print("Password too similar to an existing customer. Please enter a unique password.")
                continue
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue
            else:
                new_user.set_password(password)
                break
        self.FPlist.append(new_user)
        print("<--------! Delivery Partner Register Successful !-------->")
        for user in self.FPlist:
            print(f'UserName: {user.get_username()}\nName: {user.get_name()}\nUser Password: {user.get_password()}\nPhone Number: {user.get_number()}')
        fp_choice()

    def fp_login(self):
        print("<--------! Delivery Partner Login page !-------->")
        uN = input("Enter User Name: ")
        uP = input("Enter User Password: ")
        found_user = next((user for user in self.FPlist if user.get_username() == uN and user.get_password() == uP), None)
        if found_user:
            print("<@@@@@@ Login Successful @@@@@@>")
            self.fpoperations()
        else:
            print("Invalid login credentials")
            self.fp_login()

    def fpoperations(self):
        print("\n<-------! Delivery Partner Main Menu Page !------->")
        while True:
            print("1. View Order Details")
            print("2. Collect Order")
            print("3. Deliver the Order")
            print("4. Exit Partner")
            c = choice()
            if c == 1:
                print("\nOrders to be Collected:")
                print('-' * 30)
                if len(fcc.COlist) != 0:
                        for order in fcc.COlist:
                            if order[5] == "Not Delivered":
                                print(f"Hotel Number: {order[2]}\nDish Number: {order[3]}\nCustomer: {order[1].get_username()}\nAmount Paid: {order[4]}\nOrder ID: {order[0]}\nDelivery Status: {order[5]}")
                        print('-' * 30)
                else:
                    print("NO orders Found!")
                    print('-' * 30,"\n")
            if c == 2:
                oD = int(input("Enter the Order ID: "))
                order_found = None
                for idx, order in enumerate(fcc.COlist):
                    if order[0] == oD and order[5] == "Not Delivered":
                        order_found = list(order)
                        break
                if order_found:
                    from datetime import datetime
                    collection_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                    print(f"Order {oD} collected successfully at {collection_time}.")
                    order_found[5] = "Collected"
                    order_found.append(str(collection_time))
                    fcc.COlist[idx] = tuple(order_found)
            if c == 3:
                dO = int(input("Enter the Order ID: "))
                order_found = None
                for idx, order in enumerate(fcc.COlist):
                    if order[0] == dO and order[5] == "Collected":
                        order_found = list(order)
                        break
                if order_found:
                    from datetime import datetime
                    order_found[5] = "Delivered"
                    delivery_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                    print(f"Order {dO} delivered successfully at {delivery_time}.")
                    order_found.append(str(delivery_time))
                    print('-' * 30)
                    Partner_Issues = input("Do you have any customer issues? Mention them : ")
                    order_found.append(Partner_Issues)
                    fcc.COlist[idx] = tuple(order_found)
                    print("fcc.COlist content:", fcc.COlist)
                else:
                    print("Invalid Order Number or the order is already delivered.")
                    print('-' * 30)
            if c == 4:
                import Food_Main
                Food_Main.fm.main()

fp = food_partner()
f = fdp()