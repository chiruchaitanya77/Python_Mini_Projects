import datetime
import calendar

def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def hc_choice():
    while True:
        print("\n<------ Customer Menu ------>")
        print("1. Customer Register")
        print("2. Customer Login")
        print("3. Exit Customer Menu")
        try:
            c = choice()
            if c == 1:
                hr.hc_register()
            if c == 2:
                hr.hc_login()
            if c == 3:
                import Hotel_Main
                Hotel_Main.hm.main()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class hcustomer:
    def __init__(self):
        self.__Cname = None
        self.__Cemail = None
        self.__Cphone = None
        self.__Cpassword = None
    def set_name(self, Cname):
        self.__Cname = Cname
        return
    def get_name(self):
        return self.__Cname
    def set_email(self, Cemail):
        self.__Cemail = Cemail
        return
    def get_email(self):
        return self.__Cemail
    def set_phone(self, Cphone):
        self.__Cphone = Cphone
        return
    def get_phone(self):
        return self.__Cphone
    def set_password(self, Cpassword):
        self.__Cpassword = Cpassword
        return
    def get_password(self):
        return self.__Cpassword
    def get_customer_list(self):
        return (f'Customer Name: {hc.get_name()} \nCustomer Email: {hc.get_email} \nCustomer Phone Number: {hc.get_phone()} \nCustomer Password: {hc.get_password()}')

class hc_reg():
    HClist = []
    Rlist = [["Room1",1200], ["Room2",1500], ["Room3",1800], ["Room4",2200], ["Room5",2600], ["Room6",3000]]
    RVlist = ["Free ","Occupied","Free ","Vacated ","Free ", "Cleaned"]
    Croom = []

    def hc_register(self):
        print("\n<--------! User Register page !-------->")
        new_user = hcustomer()
        while True:
            name = input("Enter Name: ")
            if any(user.get_name() == name for user in self.HClist):
                print("Name already exists. Please enter a different name.")
                continue
            else:
                new_user.set_name(name)
                break
        while True:
            email = input("Enter Email: ")
            if any(user.get_email() == email for user in self.HClist):
                print("Email already exists. Please enter a different email.")
                continue
            else:
                new_user.set_email(email)
                break
        while True:
            try:
                no = int(input("Enter Mobile Number: "))
                if any(user.get_phone() == no for user in self.HClist):
                    print("Phone Number already exists. Please enter a different number.")
                    continue
                else:
                    new_user.set_phone(no)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        while True:
            password = input("Enter Password: ")
            if any(user.get_password() == password for user in self.HClist):
                print("Password too similar to an existing customer. Please enter a unique password.")
                continue
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue
            else:
                new_user.set_password(password)
                break
        self.HClist.append(new_user)
        print("<--------! Customer Register Successful !-------->")
        for user in self.HClist:
            print(f'Customer Name: {user.get_name()} \nCustomer Email: {user.get_email()} \nCustomer Phone Number: {user.get_phone()} \nCustomer Password: {user.get_password()}')
        hc_choice()

    def hc_login(self):
        print("\n<--------! Customer Login page !-------->")
        cN = input("Enter Customer Name: ")
        cP = input("Enter Customer Password: ")
        found_user = next((user for user in self.HClist if user.get_name() == cN and user.get_password() == cP), None)
        if found_user:
            print("<@@@@@@ Login Successful @@@@@@>")
            self.hcoperations(found_user)
        else:
            print("Invalid login credentials")
            self.hc_login()

    def hcoperations(self, logged_in_customer):
            while True:
                print("\n<-------! Customer Main Menu Page !------->")
                print("1. View/Book Rooms")
                print("2. Vacate Room")
                print("3. Back to Main Menu")
                c = choice()
                if c == 1:
                    hr.vb_rooms(logged_in_customer)
                if c == 2:
                    while True:
                        try:
                            vacate_ri = int(input("Enter the Room Number to Vacate: ")) - 1
                            check = next((entry for entry in hr.Croom if entry[0] == logged_in_customer and entry[1] == vacate_ri), None)
                            if check:
                                hr.Croom.remove(check)
                                hr.RVlist[vacate_ri] = "Vacated "
                                print(f"Room {hr.Rlist[vacate_ri][0]} vacated successfully by {logged_in_customer.get_name()}.")
                                print("##################------>Thank you for using our services. Visit again soon.<------##################")
                                break
                            else:
                                print("You have not booked this room. Try again.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                if c == 3:
                    import Hotel_Main
                    Hotel_Main.hm.main()
                else:
                    print("Invalid choice. Please try again.")

    def vb_rooms(self, logged_in_customer):
            print("<--------------------! View/Book Rooms Page !-------------------->")
            print("\n<--------------------! AVAILABLE ROOMS !-------------------->")
            for rv, r in zip(hr.RVlist, hr.Rlist):
                if rv == "Free ":
                    print(f"|  Room Num: {r[0]}\t |\t Price: {r[1]}   |\tVacency: {rv}\t|")
                    print('-' * 61)
            while True:
                print("<--------- Room Booking Page !-------->")
                print("1. Book Room ")
                print("2. Back to Menu")
                c = choice()
                if c == 1:
                    while True:
                        print("1. Book Room Now")
                        print("2. Book Room for Later")
                        c = choice()
                        if c == 1:
                            while True:
                                try:
                                    ri = int(input("Enter the Room Number: ")) - 1
                                    if 0 <= ri < len(hr.Rlist) and hr.RVlist[ri] == "Free ":
                                        print('-' * 30)
                                        print(f"Room Details: {hr.Rlist[ri][0]} \nPrice: Rs.{hr.Rlist[ri][1]}")
                                        print('-' * 30)
                                        break
                                    else:
                                        print("Room is already booked or Invalid room number. Please try again.")
                                        continue
                                except ValueError:
                                    print("Invalid input. Please enter a valid date or number.")
                            pay = input("Do you want to pay now? (Y/N) : ")
                            while True:
                                if pay.lower() == "y":
                                    pay_amount = int(input(f"Enter Payment Amount of Rs.{hr.Rlist[ri][1]}: "))
                                    if pay_amount == hr.Rlist[ri][1]:
                                        print("Payment Successful ✅")
                                        hr.RVlist[ri] = "Occupied"
                                        hr.Croom.append((logged_in_customer, ri))
                                        current_date = datetime.datetime.now().date()
                                        current_time = datetime.datetime.now().time().strftime("%I:%M %p")
                                        out_time = (datetime.datetime.now() + datetime.timedelta(hours=12)).time().strftime("%I:%M %p")
                                        print("Booked On Date:", current_date)
                                        print("Booked At Time:", current_time)
                                        print("Log Out on or Before:", out_time, "<<<----")
                                        hr.hcoperations(logged_in_customer)
                                    else:
                                        print(f"Payment Failed. Required amount is Rs.{hr.Rlist[ri][1]}")
                                        continue
                                elif pay.lower() == "n":
                                    print("Payment Cancelled ... Returning to Main Menu.")
                                    hr.hcoperations(logged_in_customer)

                        if c == 2:
                            while True:
                                try:
                                    booking_date = input("Enter the Booking Date (YYYY-MM-DD): ")
                                    booking_date = datetime.datetime.strptime(booking_date, "%Y-%m-%d").date()
                                    if booking_date < datetime.datetime.now().date():
                                        print("Booking date cannot be in the past. Please try again.")
                                        continue
                                    ri = int(input("Enter the Room Number: ")) - 1
                                    if 0 <= ri < len(hr.Rlist) and hr.RVlist[ri] == "Free ":
                                        print('-'*30)
                                        print(f"Room Details: {hr.Rlist[ri][0]} \nPrice: Rs.{hr.Rlist[ri][1]}")
                                        print('-' * 30)
                                        break
                                    else:
                                        print("Room is already booked or Invalid room number. Please try again.")
                                        continue
                                except ValueError:
                                    print("Invalid input. Please enter a valid date or number.")
                            pay = input("Do you want to pay now? (Y/N) : ")
                            while True:
                                if pay.lower() == "y":
                                    pay_amount = int(input(f"Enter Payment Amount of Rs.{hr.Rlist[ri][1]}: "))
                                    if pay_amount == hr.Rlist[ri][1]:
                                        print("Payment Successful ✅")
                                        print(f"Room {hr.Rlist[ri][0]} booked successfully to Customer {logged_in_customer.get_name()} on {booking_date}.")
                                        hr.RVlist[ri] = "Occupied"
                                        hr.Croom.append((logged_in_customer, ri, str(booking_date)))
                                        hr.hcoperations(logged_in_customer)
                                    else:
                                        print(f"Payment Failed. Required amount is Rs.{hr.Rlist[ri][1]}")
                                        continue
                                elif pay.lower() == "n":
                                    print("Payment Cancelled ... Returning to Main Menu.")
                                    hr.hcoperations(logged_in_customer)

                if c == 2:
                    hr.hcoperations(logged_in_customer)
                else:
                    print("Invalid choice. Please try again.")
hc = hcustomer()
hr = hc_reg()