class Travel:
    name = "Adam"
    citizen = "Malaysia"
    
        
travel_detail = Travel()

print("Person's name: ", hasattr(travel_detail, "citizen"))
print("Person's address: ", hasattr(travel_detail, "address"))

