# Andrew Seabolt
# Module 3 Lab - Case Study: Lists, Functions, and Classes

# A super class called Vehicle, for vehicle type such as car, truck, plane, boat or a broomstick

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# a class called Automobile which will inherit the attributes from Vehicle and also contain other attributes:

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    print("Please enter vehicle details: ")

    vehicle_type = "car"

    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter # of doors (2 or 4): ")
    roof = input("Enter roof type (solid or sun roof: ")

    my_car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\n--- Vehicle Info ---")
    print(f"Vehicle type: {my_car.vehicle_type}")
    print(f"Year: {my_car.year}")
    print(f"Make: {my_car.make}")
    print(f"Model: {my_car.model}")
    print(f"Number of Doors: {my_car.doors}")
    print(f"Type of Roof: {my_car.roof}")

if __name__ == "__main__":
    main()
# Output should look like:

# Vehicle Type: car
# Year: 2022
# Make: Toyota
# Model: Corolla
# Number of Doors: 4
# Roof Type: sun roof


