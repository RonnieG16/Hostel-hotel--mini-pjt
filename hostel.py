from datetime import datetime

class Visit:
    def __init__(self, friend, room, reason):
        self.friend = friend
        self.room = room
        self.reason = reason
        self.time_in = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_out = None  # initially empty

    def check_out(self):
        self.time_out = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"Friend: {self.friend}, Room: {self.room}, Reason: {self.reason}, "
                f"Time In: {self.time_in}, Time Out: {self.time_out if self.time_out else 'Not yet checked out'}")

class HostelVisitSystem:
    def __init__(self):
        self.visits = []

    def add_visit(self):
        friend = input("Enter friend's name: ")
        room = input("Enter room number: ")
        reason = input("Reason for visit: ")

        visit = Visit(friend, room, reason)
        self.visits.append(visit)
        print("✅ Visit recorded!\n")

    def view_visits(self):
        if not self.visits:
            print("No visits recorded yet.\n")
            return
        for i, v in enumerate(self.visits, start=1):
            print(f"\nVisit {i}")
            print(v)

    def check_out(self):
        if not self.visits:
            print("No visits recorded yet.\n")
            return

        self.view_visits()
        try:
            choice = int(input("\nEnter the visit number to check out: "))
            if 1 <= choice <= len(self.visits):
                visit = self.visits[choice - 1]
                if visit.time_out:
                    print("⚠ Already checked out!")
                else:
                    visit.check_out()
                    print("✅ Checked out successfully!\n")
            else:
                print("Invalid visit number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    def menu(self):
        while True:
            print("\n--- Hostel Visit System ---")
            print("1. Add Visit")
            print("2. View Visits")
            print("3. Check Out")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_visit()
            elif choice == "2":
                self.view_visits()
            elif choice == "3":
                self.check_out()
            elif choice == "4":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, try again.\n")

# Run the program
system = HostelVisitSystem()
system.menu()
