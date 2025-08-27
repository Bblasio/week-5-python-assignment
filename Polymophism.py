# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Polymorphic behavior
