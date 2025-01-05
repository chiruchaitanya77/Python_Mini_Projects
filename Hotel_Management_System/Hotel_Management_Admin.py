from Hotel_Customer import hr
def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class hadmin:
    name = "ad"
    password = "123"
    def a_login(self):
        print("\n<--------! Admin Login page !-------->")
        cN = input("Enter Admin Name: ")
        cP = input("Enter Admin Password: ")
        if cN == self.name and cP == self.password:
            print("<@@@@@@ Login Successful @@@@@@>")
            self.aoptions()
        else:
            print("Invalid login credentials")
            self.a_login()

    def aoptions(self):
        print("\n-----! HOTEL ADMIN PANEL !-----")
        while True:
            print("1. Free Rooms")
            print("2. Exit Admin")
            c = choice()
            if c == 1:
                self.open()
                break
            elif c == 2:
                import Hotel_Main
                Hotel_Main.hm.main()
                break
            else:
                print("Invalid choice. Please try again.")
                continue
    def open(self):
        print("\n<---------------! CLEANED ROOMS !--------------->")
        cleaned_rooms = [r for rv, r in zip(hr.RVlist, hr.Rlist) if rv == "Cleaned"]
        if not cleaned_rooms:
            print("No rooms pending to be Ready")
        else:
            for rv, r in zip(hr.RVlist, hr.Rlist):
                if rv == "Cleaned":
                    print(f"|  Room Num: {r[0]}\t|\tCleaned rooms: {rv}\t|")
                    print('-' * 49)
        while True:
            try:
                # After entering room number, check if the room is vacated.
                v_ri = int(input("Enter Room Number to Free: ")) - 1
                if v_ri >= 0 and v_ri < len(hr.Rlist) and hr.RVlist[v_ri] == "Cleaned":
                    hr.RVlist[v_ri] = "Free "
                    print(f"Room {hr.Rlist[v_ri][0]} is Ready to be booked .")
                    ha.aoptions()
                else:
                    print("Room is not vacated or not cleaned. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

ha = hadmin()