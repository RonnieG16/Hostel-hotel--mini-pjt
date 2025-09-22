from datetime import datetime


class Visitor:
    def __init__(self, name, room_number, reason_for_visit):
        self.name = name
        self.room_number = room_number
        self.reason_for_visit = reason_for_visit
        self._check_in_time = datetime.now()  
        self._is_checked_in = True  
    
    def check_out(self):
        if self._is_checked_in:
            self._is_checked_in = False
            return f"{self.name} checked out."
        return f"{self.name} is already checked out."
    
    def get_info(self):
        status = "Checked in" if self._is_checked_in else "Checked out"
        return f"Visitor: {self.name}, Room: {self.room_number}, Reason: {self.reason_for_visit}, Status: {status}"


class VIPVisitor(Visitor):
    def __init__(self, name, room_number, reason_for_visit, vip_note):
        super().__init__(name, room_number, reason_for_visit)
        self.vip_note = vip_note  
    
    def get_info(self):  
        status = "Checked in" if self._is_checked_in else "Checked out"
        return (f"VIP Visitor: {self.name}, Room: {self.room_number}, "
                f"Reason: {self.reason_for_visit}, VIP Note: {self.vip_note}, Status: {status}")


class Hostel:
    def __init__(self):
        self.visitors = []  
    
    def add_visitor(self, visitor):
        self.visitors.append(visitor)
        return f"{visitor.name} added to the hostel."
    
    def check_out_visitor(self, name):
        for visitor in self.visitors:
            if visitor.name == name:
                return visitor.check_out()
        return f"Visitor {name} not found."
    
    def show_all_visitors(self):
        if not self.visitors:
            return "No visitors in the hostel."
        return "\n".join([visitor.get_info() for visitor in self.visitors])

 
if __name__ == "__main__":
    hostel = Hostel()
    
    
    visitor1 = Visitor("Annet", "101", "Visiting friend")
    visitor2 = VIPVisitor("Ronald", "201", "Group discussion", "Needs to work on assignments")
    
    
    print(hostel.add_visitor(visitor1))  
    print(hostel.add_visitor(visitor2))  
    
    # Show all visitors
    print("\nAll Visitors:")
    print(hostel.show_all_visitors())
    
    # Check out a visitor
    print("\nChecking out Alice:")
    print(hostel.check_out_visitor("Alice"))
    
    # Show all visitors again
    print("\nAll Visitors:")
    print(hostel.show_all_visitors())
