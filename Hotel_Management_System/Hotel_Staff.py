from Hotel_Customer import hr
def choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class hstaff:
    def soptions(self):
        print("\n-----! HOTEL STAFF PANEL !-----")
        print("1. Cleaning Rooms")
        print("2. Exit Staff")
        c = choice()
        if c == 1:
            self.remind()
        if c == 2:
            import Hotel_Main
            Hotel_Main.hm.main()
        else:
            print("Invalid choice. Please try again.")
    def remind(self):
        print("\n<---------------! VACATED ROOMS !--------------->")
        vacated_rooms = [r for rv, r in zip(hr.RVlist, hr.Rlist) if rv == "Vacated "]
        if not vacated_rooms:
            print("No rooms pending to clean")
            hs.soptions()
        else:
            for rv, r in zip(hr.RVlist, hr.Rlist):
                if rv == "Vacated ":
                    print(f"|  Room Num: {r[0]}\t|\tTo be Cleaned: {rv}\t|")
                    print('-' * 49)
        while True:
            try:
                # After entering room number, check if the room is vacated.
                v_ri = int(input("Enter the Room Number to Clean: ")) - 1
                if v_ri >= 0 and v_ri < len(hr.Rlist) and hr.RVlist[v_ri] == "Vacated ":
                    hr.RVlist[v_ri] = "Cleaned"
                    print(f"Room {hr.Rlist[v_ri][0]} is Cleaned successfully.")
                    hs.remind()
                else:
                    print("Invalid entry or the room is not vacated. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


hs = hstaff()