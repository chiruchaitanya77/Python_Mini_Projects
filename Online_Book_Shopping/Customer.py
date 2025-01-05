'''
4. Book Shop
Author: Chiru Chaitanya
Date: 2021-09-20
Description: This is a book shop application that allows customers to buy and sell books.

Structure:
- Show Welcome to 4. Book Shop Message
    - Show Main Menu
        - 1. Admin/Accounts
        - 2. Customer
1. Admin
2. Customer
    - 1. Register
        - UserName
        - UserEmail
        - UserPassword
        - Confirm Password
        - UserStatus After successful Registration
            - Back to Main Menu
    - 2. Login
        - UserName
        - UserPassword
        - Account Activation is done after depositing 1000 rupees and not less
            - Deposit 1000 rupees
                - Back to Main Menu to login again
            - Show Welcome Message
            - Show Main Menu
                - 1. Buy Book
                    - Enter Book Name
                        - If book is present in stock
                            - Show Book Details
                            - Show Total Price
                            - Bargain Price in loop until customer makes OK or Minimum set Price for book limit reached
                                - Show Total Price
                                - Show Bargain Price
                                - Show Payment Amount
                                - Show Payment Status
                                - Display Happy Reading Message
                                    - Back to Main Menu to go back to Main Menu
                - 2. Sell Book
                    - Enter Book Name
                    - Enter Price
                - 3. Search for Book
                    - Enter Book Name
                        - Show Book Details
                        - Back to Main Menu to go back to Main Menu
                - 4. Exit 4. Book Shop
                    - Back to Main Menu
    - 3. Exit
        - Back to Main Menu
    - 4. Delete Account
        - Enter UserName
        - Enter UserPassword
        - Confirm Password
        - Show Confirmation Message for Delete Account
            - If Yes
                - Delete Account from Database
            - If No
                - Back to Main Menu to go back to Main Menu
3. Exit 4. Book Shop
    - Show Goodbye Message
            - Exit 4. Book Shop
'''
from symbol import continue_stmt


class cr:
    def __init__(self):
        self.__Cname = None
        self.__Cemail = None
        self.__Cpassword = None
        self.__Cstatus = None

    def set_name(self,Cname):
        self.__Cname = Cname
        return

    def get_name(self):
        return self.__Cname

    def set_email(self,Cemail):
        self.__Cemail = Cemail
        return

    def get_email(self):
        return self.__Cemail

    def set_password(self,Cpassword):
        self.__Cpassword = Cpassword
        return

    def get_password(self):
        return self.__Cpassword

    def set_status(self,Cstatus):
        self.__Cstatus = Cstatus
        return

    def get_status(self):
        return self.__Cstatus

    def get_customer_list(self):
        return (f'User Name: {c.get_name()}\nUser Email: {c.get_email}\nUser Password: {c.get_password()}\nUser Status: {c.get_status()}')

def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def per(a):
    return int(a*0.745)

def us_choice():
    while True:
        print("<------ Customer Menu ------>")
        print("1. Register")
        print("2. Login")
        print("3. Exit Customer Menu")
        try:
            c = choice()
            if c == 1:
                r.register()
            if c == 2:
                r.c_login()
            if c == 3:
                import main
                main.m.main()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


class reg():
    Clist = []
    Blist = [("Book1", 200), ("Book2", 300), ("Book3", 400), ("Book4", 500), ("Book5", 600),
             ("Book6", 700), ("Book7", 800), ("Book8", 900), ("Book9", 1000), ("Book10", 1100)]
    def register(self):
        print("<--------! User Register page !-------->")
        new_user = cr()
        while True:
            name = input("Enter Name: ")
            if any(user.get_name() == name for user in self.Clist):
                print("Name already exists. Please enter a different name.")
                continue
            else:
                new_user.set_name(name)
                break
        while True:
            email = input("Enter Email: ")
            if any(user.get_email() == email for user in self.Clist):
                print("Email already exists. Please enter a different email.")
                continue
            else:
                new_user.set_email(email)
                break
        while True:
            password = input("Enter Password: ")
            if any(user.get_password() == password for user in self.Clist):
                print("Password too similar to an existing customer. Please enter a unique password.")
                continue
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue
            else:
                new_user.set_password(password)
                break
        new_user.set_status("Deactivated")
        self.Clist.append(new_user)
        print("<--------! User Register Successful !-------->")
        for user in self.Clist:
            print(f'User Name: {user.get_name()} \nUser Email: {user.get_email()} \nUser Password: {user.get_password()} \nUser Status: {user.get_status()}')
        us_choice()

    def c_login(self):
        print("<--------! User Login page !-------->")
        uN = input("Enter User Name: ")
        uP = input("Enter User Password: ")
        #For searching uN,uP pair in entire list
        found_user = next((user for user in self.Clist if user.get_name() == uN and user.get_password() == uP), None)
        if found_user:
            print("<@@@@@@ Login Successful @@@@@@>")
            self.operations()
            # if found_user.get_status() == "Deactivated":
            #     print("***** WARNING *****\nYour account is deactivated. Please contact Admin for further details.")
            #     import main
            #     main.m.main()
            # else:
            #     self.operations()
        else:
            print("Invalid login credentials")
            self.c_login()

    def operations(self):
        while True:
            print("\nHere are the User Operations available :")
            print("1. Buy Book")
            print("2. Sell Book")
            print("3. Search for Book")
            print("4. Delete Account")
            print("5. Exit")
            try:
                c = choice()
                if c == 1:
                    r.buy()
                elif c == 2:
                    r.sell()
                elif c == 3:
                    r.search()
                elif c == 4:
                    r.delete()
                elif c == 5:
                    import main
                    main.m.main()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def buy(self):
        print("<--------! Buy Book page !-------->")
        book_name = input("Enter Book Name: ")
        if book_name not in [book[0] for book in self.Blist]:
            print("Book not found in stock. Please try again.")
            r.buy()
        else:
            for book in self.Blist:
                if book[0] == book_name:
                    print("<------ Book Details ------>")
                    print(f"Book Name: {book[0]}\nBook Price: Rs.{book[1]}")
                    print("-"*30)
                    total_price = book[1]
                    bargain_price = per(total_price)
                    while True:
                        while True:
                            try:
                                user_bargain_price = int(input("Enter Bargain Price: "))
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                                continue
                        if bargain_price >= user_bargain_price <= total_price:
                            print("Your Bargain Price is less than Buying Price. Please try again.")
                            continue
                        else:
                            break
                    print(f"1. Buy book for price of Rs.{user_bargain_price}")
                    print(f"2. Cancel Buying")
                    c = choice()
                    if c == 1:
                        print(f"Payment of Rs.{user_bargain_price} is Successful")
                        print(f"Enjoy Reading our Book {book[0]} !!!")
                    if c == 2:
                        print("Book Payment Cancelled. Returning to Main Menu.")
                        r.buy()
    def sell(self):
        print("<--------! Sell Book page !-------->")
        book_name = input("Enter Book Name: ")
        while True:
            book_price = int(input("Enter Price: "))
            bargain_price = per(book_price)
            while True:
                while True:
                    try:
                        seller_bargain_price = int(input("Enter Bargain Price: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue
                if bargain_price >= seller_bargain_price <= book_price:
                    print("Book Price is too High. Please try again.")
                    continue
                else:
                    break
            print(f"1. Sell book for price of Rs.{seller_bargain_price}")
            print(f"2. Cancel Selling")
            c = choice()
            if c == 1:
                print(f"Payment of Rs.{seller_bargain_price} is Successful")
                print(f"ThankYou for selling the Book {book_name} !!!")
            if c == 2:
                print("Book Selling Cancelled. Returning to Main Menu.")
                r.sell()

    def search(self):
        print("<--------! Search Book page !-------->")
        book_name = input("Enter Book Name: ")
        if book_name not in [book[0] for book in self.Blist]:
            print("Book not found in stock. Please try again.")
            r.buy()
        else:
            for book in self.Blist:
                if book[0] == book_name:
                    print("<------ Book Details ------>")
                    print(f"Book Name: {book[0]}\nBook Price: Rs.{book[1]}")
                    print("-" * 30)
            while True:
                print("1. Wanna Buy the Book")
                print("2. Continue Search")
                print("3. Back to Main Menu")
                c = choice()
                if c == 1:
                    r.buy()
                if c == 2:
                    r.search()
                if c == 3:
                    r.operations()

    def delete(self):
        print("<--------! User Deletion page !-------->")
        uN = input("Enter User Name: ")
        uP = input("Enter User Password: ")
        # For searching uN,uP pair in entire list
        found_user = next((user for user in self.Clist if user.get_name() == uN and user.get_password() == uP), None)
        if found_user:
            print("<------ Account Delete Page !------->")
            print("User Found: " + found_user.get_name())
        else:
            print("Invalid login credentials")
            self.delete()
        while True:
            print("1. Delete Account")
            print("2. Cancel")
            c = choice()
            if c == 1:
                self.Clist.remove(found_user)
                print("Account deleted successfully.")
                us_choice()
                break
            if c == 2:
                r.operations()
                break
c = cr()
r = reg()