class Tsavaari:
    usernames = {}
    STATIONS = [
        "Ameerpet", "S.R. Nagar", "ESI Hospital", "Erragadda",
        "Bharat Nagar", "Moosapet", "Balanagar", "Kukatpally",
        "KPHB", "JNTUH", "Miyapur"
    ]

    def __init__(self, name, age, email, gender, phone, password):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
        self.phone = phone
        self.password = password
        self.booked = []
        self.logged = False
        Tsavaari.usernames[name] = self
    @classmethod
    def register(cls):
        print("\n=== REGISTER ===")
        while True:
            name = input("Enter username: ").strip()
            if name in cls.usernames:
                print("Username already exists. Try another.\n")
            elif not name:
                print("Username cannot be empty.\n")
            else:
                break

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age entered. Registration failed.")
            return None

        if age < 18:
            print("Registration Failed: Age must be 18 years or above.")
            return None

        email = input("Enter email: ").strip()
        gender = input("Enter gender: ").strip()
        phone = input("Enter phone number: ").strip()

        while True:
            password = input("Create password (at least 8 characters): ")
            if len(password) >= 8:
                break
            print("Password too short! Must be at least 8 characters.")
        user = cls(name, age, email, gender, phone, password)
        print("\nRegistration Successful!")
        user.logged = True
        user.profile()
        return user

    @classmethod
    def login_system(cls):
        print("\n=== LOGIN ===")
        un = input("Enter username: ").strip()
        pw = input("Enter password: ")

        if un in cls.usernames and cls.usernames[un].password == pw:
            user = cls.usernames[un]
            user.logged = True
            print(f"\nWelcome back, {user.name}!")
            user.profile()
            return user
        else:
            print("Invalid username or password.")
            return None
    def profile(self):
        while self.logged:
            print("\n=== PROFILE ===")
            print(f"Name  : {self.name}")
            print(f"Phone : {self.phone}")
            print(f"Email : {self.email}")
            print("-" * 20)
            print("1. Book Ticket")
            print("2. More Options")
            print("3. Logout")

            choice = input("Enter choice (1-3): ").strip()

            if choice == "1":
                self.book()
            elif choice == "2":
                self.more()
            elif choice == "3":
                self.logout()
                break
            else:
                print("Invalid option! Please enter 1, 2, or 3.")

    def book(self):
        print("\n=== BOOK TICKET ===")
        print("Available Stations:")
        for idx, station in enumerate(self.STATIONS, 1):
            print(f"{idx}. {station}")
        print("-" * 20)

        src = input("From station: ").strip()
        dst = input("Destination station: ").strip()

        if src not in self.STATIONS or dst not in self.STATIONS:
            print("Invalid Station(s). Please choose from the list.")
            return

        if src == dst:
            print("Source and Destination cannot be the same!")
            return
        fare = abs(self.STATIONS.index(dst) - self.STATIONS.index(src)) * 10
        print(f"\nTotal Fare: {fare}/-")

        pin = input("Enter 4-digit PIN to pay: ").strip()
        if len(pin) == 4 and pin.isdigit():
            print("Payment Successful!")
            ticket_details = f"{src} --> {dst} | Fare: {fare}/-"
            self.booked.append(ticket_details)

            ch = input("\nEnter 1 to view ticket, or press Enter to return: ").strip()
            if ch == "1":
                print(f"\n--- TICKET CONFIRMATION ---\n{ticket_details}\n---------------------------")
                input("Press Enter to continue...")
        else:
            print("Payment Failed: Invalid 4-digit PIN.")

    def logout(self):
        if self.logged:
            self.logged = False
            print("\nLogout Successful!")
        else:
            print("\nAlready logged out.")

    def more(self):
        while self.logged:
            print("\n=== MORE OPTIONS ===")
            print("1. Change Password")
            print("2. View Booking History")
            print("3. Logout")
            print("4. Back to Profile")

            op = input("Enter choice (1-4): ").strip()

            if op == "1":
                pw = input("Enter current password: ")
                if pw == self.password:
                    new_pw = input("Enter new password (min 8 chars): ")
                    if len(new_pw) >= 8:
                        self.password = new_pw
                        print("Password changed successfully!")
                    else:
                        print("Password change failed: New password too short.")
                else:
                    print("Incorrect current password.")
            elif op == "2":
                print("\n=== BOOKING HISTORY ===")
                if not self.booked:
                    print("No bookings found.")
                else:
                    for i, ticket in enumerate(self.booked, 1):
                        print(f"{i}. {ticket}")
                input("\nPress Enter to continue...")
            elif op == "3":
                self.logout()
                break
            elif op == "4":
                break
            else:
                print("Invalid option!")


if __name__ == "__main__":
    user1 = Tsavaari.register()