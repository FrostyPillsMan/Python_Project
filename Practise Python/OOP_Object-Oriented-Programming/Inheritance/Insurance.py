class Vehicle:
    def __init__(self, is_second_hand, age_on_road, no_of_wheels=0, no_of_seats=0):
        self.no_of_wheels = no_of_wheels
        self.no_of_seats = no_of_seats
        self.is_second_hand = is_second_hand
        self.age_on_road = age_on_road

    def check_if_second_hand(self):
        print("Checking if a vehicle is second hand...")
        return self.is_second_hand
    
    def get_age_on_road(self):
        print("Getting age on road...")
        return self.age_on_road

# Class inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, is_second_hand, age_on_road):
        super().__init__(is_second_hand, age_on_road, 2, 2)

class Insurance:
    def __init__(self, vehicle: Vehicle, amount):
        self.vehicle = vehicle  # Composition
        self.amount = amount

    def describe_vehicle(self):
        is_second_hand = self.vehicle.check_if_second_hand()
        vehicle_age = self.vehicle.get_age_on_road()
        return is_second_hand, vehicle_age


# Example usage
bike_obj = Bike(True, 4)
insurance = Insurance(bike_obj, 50000)
details = insurance.describe_vehicle()
print(
    f"Vehicle Details after Constructing ==> Second Hand: {details[0]}, Age on Road: {details[1]}"
)

