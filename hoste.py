class Resisdent:
    def __init__(self, name, id, room, capacity, phone_number):
        self.id = id
        self.name = name
        self.room = room
        self.capacity = capacity
        self.phone_number= phone_number
        
    def R_info(self):
        print(f"The resident is {self.name} with an ID number {self.id} in room {self.room}")
        
class visitor:
    def __init__(self, name, room, reason, phone_number, time_in, time_out):
        self.name = name
        self.room = room
        self.reason = reason
        self.phone_number = phone_number
        self.time_in = time_in
        self.time_out =time_out
        
    def show_visits(self):
        print(f"The visitor is {self.name} with an ID number {self.phone_number}. The time they have entered the hostel is {self.time_in} and they left at {self.time_out}. The reason for their visit: {self.reason}")
        
class Hostel:
    def __init__(self, H_name, H_location, castodian_phone):
        self.H_name = H_name
        self.H_location = H_location
        self.castodian_phone = castodian_phone
        self.visits = []
        
    def H_info(self):
        print(f"welcome to {self.H_name}, at {self.H_location},for any inquiries call {self.castodian_phone}")
            
            
visitor1 = visitor("Samantha", "-5", "Just checking", "123456789", "12:05 pm", "2:00 pm")
visitor2 = visitor("Merinah", "-12", "Finalizing group work", "987654321", "3:05 pm", "4:45 pm")
visitor3 = visitor("Nothing", "-3", "Professional Visit", "456789123", "11:03 am", "2:50 pm")

res1 = Resisdent("Samuel", "B3", "-5", 1, "123456789")
res2 = Resisdent("Mary", "V4", "-12", 1, "987654321")
res3 = Resisdent("Sammy", "M2", "-3", 1, "456789123")

hos1 = Hostel("Sarameck Hostel", "Wandegeya", "111222333")
hos2 = Hostel("David's Ark", "Bugujju", "444555666")
hos3 = Hostel("PDR Hostel", "Bugujju", "777888999")



#visitor1.V_info()
res2.R_info()
hos3.H_info()
visitor1.show_visits()
        
        
        
        