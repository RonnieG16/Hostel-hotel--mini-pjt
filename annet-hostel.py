import datetime

class Visit:
    def __init__(self, name, room, reason):
        self.name = name              
        self.room = room              
        self.reason = reason          
        self.time_in = datetime.datetime.now()  
        self.time_out = None         

    # Mark visitor as checked out
    def check_out(self):
        if self.time_out:  
            print(f"⚠ {self.name} already checked out.")
        else:              
            self.time_out = datetime.datetime.now()
            print(f"✅ {self.name} checked out.")

    # visit details 
    def __str__(self):
    
        if self.time_out:
            out_time = self.time_out.strftime("%H:%M:%S")
        else:
            out_time = "Still inside"

        details = (
            f"Friend: {self.name}\n"
            f"Room: {self.room}\n"
            f"Reason: {self.reason}\n"
            f"Time In: {self.time_in.strftime('%H:%M:%S')}\n"
            f"Time Out: {out_time}"
        )
        return details


# Class to manage multiple visits
class HostelVisitSystem:
    def __init__(self):
        self.visits = []  

    # Add a new visit
    def add_visit(self):
        name = input("Friend's name: ")
        room = input("Room number: ")
        reason = input("Reason: ")
        self.visits.append(Visit(name, room, reason))
        print("✅ Visit added.\n")

    # View all visits
    def view_visits(self):
        if not self.visits:
            print("⚠ No visits yet.\n")
        else:
            for i, visit in enumerate(self.visits, 1):
                print(f"\nVisit {i}:\n{visit}\n")

    # Check out a visitor
    def check_out(self):
        self.view_visits()
        try:
            choice = int(input("Visit number to check out: "))
            self.visits[choice - 1].check_out()
        except (ValueError, IndexError):
            print("⚠ Invalid choice.\n")

    # Main menu loop
    def run(self):
        while True:
            print("\n--- Hostel Visit System ---")
            print("1. Add Visit")
            print("2. View Visits")
            print("3. Check Out")
            print("4. Exit")

            choice = input("Choose: ")
            if choice == "1":
                self.add_visit()
            elif choice == "2":
                self.view_visits()
            elif choice == "3":
                self.check_out()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("⚠ Invalid option.\n")


# Run the system
if __name__ == "__main__":
    HostelVisitSystem().run()
