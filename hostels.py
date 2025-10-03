class Resident:
    def __init__(self, name, room_no):
        self.name = name
        self.room_no = room_no

class Visitor:
    def __init__(self, name, visitor_ID,):
        self.name = name
        self.visitor_ID = visitor_ID
        
        

class Hostel:
    def __init__(self, name):
        self.name = name 
        self.visits =[]
    def record_visit(self, visitor: Visitor, resident: Resident):
        entry = visitor.name + " is visiting " + resident.name + " in room " + str(resident.room_no)
        self.visits.append(entry)

    def show_visits(self):
        print(f"visit log for {self.name} Hostel:")
        if not self.visits:
            print("No visits recorded yet!!")
        for visit in self.visits:
            print("_"+ visit)
        
#demo
hostel = Hostel("PDR")
resident = Resident("BOB", 123)

Visitor1 = Visitor("ALICE", "V1")
Visitor2 = Visitor("CHARLIE", "V2")
Visitor3 = Visitor("DAVID", "V3")
Visitor4 = Visitor("EVE", "V4")

hostel.record_visit(Visitor1, resident)
hostel.record_visit(Visitor2, resident)
hostel.record_visit(Visitor3, resident)
hostel.record_visit(Visitor4, resident)

hostel.show_visits()





