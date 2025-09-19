from datetime import datetime

class Visit:
    def _init_(self, friend, room, reason, time_out=""):
        self.friend = friend
        self.room = room
        self.reason = reason
        self.time_in = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_out = time_out

    def _str_(self):
        return (f"Friend: {self.friend}, Room: {self.room}, Reason: {self.reason}, "
                f"Time In: {self.time_in}, Time Out: {self.time_out}")

class HostelVisitSystem:
    def _init_(self):
        self.visits = []

    def add_visit(self):
        friend = input("Enter friend's name: ")
        room = input("Enter room number: ")
        reason = input("Reason for visit: ")
        time_out = input("Enter time out (optional): ")

        visit = Visit(friend, room, reason, time_out)
        self.visits.append(visit)
        print("✅ Visit recorded!\n")

    def view_visits(self):
        if not self.visits:
            print("No visits recorded yet.\n")
            return
        for i, v in enumerate(self.visits, start=1):
            print(f"\nVisit {i}")
            print(v)

    def menu(self):
        while True:
            print("\n--- Hostel Visit System ---")
            print("1. Add Visit")
            print("2. View Visits")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_visit()
            elif choice == "2":
                self.view_visits()
            elif choice == "3":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, try again.\n")

# Run the program
system = HostelVisitSystem()
system.menu()
