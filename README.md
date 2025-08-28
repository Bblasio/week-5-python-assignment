# Python week 5 assignment
Welcome to my Python Object-Oriented Programming (OOP) assignment showcase 

---
## Overview  
This assignment focuses on applying the principles of Object-Oriented Programming (OOP) in Python. The goal is to model real-world entities using classes, attributes, and methods while demonstrating the four main pillars of OOP: encapsulation, inheritance, polymorphism, and abstraction.
The assignment is divided into two activities:

### 🔹 Activity 1: Smartphone Class with Encapsulation and Inheritance

This activity involves designing a `Smartphone` class that models a digital device with attributes like brand, model, and battery life. The class uses a constructor to initialize each object with unique values.

- **Encapsulation** is implemented using private attributes (`__attribute`) and controlled access via getter and setter methods.
- A subclass `GamingPhone` extends the base class, introducing specialized attributes and overriding methods to demonstrate **inheritance** and **polymorphism**.

> ✅ **Outcome:**
> - Mastery of class construction and object initialization  
> - Secure attribute handling through encapsulation  
> - Clear demonstration of inheritance and method overriding  
> - Ability to model specialized behavior in subclasses

---

### 🔹 Activity 2: Polymorphism with Vehicle Classes

This activity focuses on **polymorphism** by creating a base `Vehicle` class with a common method `move()`. Subclasses such as `Car`, `Plane`, and `Boat` override this method to reflect unique movement behaviors.

- Each subclass defines its own version of `move()`, illustrating how a shared interface can produce different outcomes depending on the object type.

> ✅ **Outcome:**
> - Strong grasp of polymorphism through method overriding  
> - Design of flexible systems with shared interfaces  
> - Clear understanding of behavioral variation across classes  
> - Reinforcement of clean, modular code structure


---

##  Project Structure

---

##  Activity 1: Smartphone Class  
##  File Structure  
smartphone.py
### 🔹 Features
- Attributes:  
  - `brand`  
  - `model`  
  - `__storage` (private, encapsulated)  
- Methods:  
  - `call()` → Simulates making a call  
  - `info()` → Displays phone details  
  - `get_storage()` & `set_storage()` → Encapsulation in action  
- Inheritance:  
  - `GamingPhone` extends `Smartphone` and adds `play_game()`  

### Example Code
```
# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage   # private attribute (encapsulation)

    # Getter method for storage
    def get_storage(self):
        return self.__storage

    # Setter method for storage
    def set_storage(self, storage):
        self.__storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.__storage}GB")


# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # initialize parent attributes
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game}!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S25 Ultra", 128)
phone1.info()
phone1.call("+254712345678")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, "Adreno 730")
gaming_phone.info()
gaming_phone.play_game("eFOOTBALL")
```
 # Expected Output
Brand: Samsung, Model: Galaxy S25 Ultra, Storage: 128GB  
Samsung Galaxy S25 Ultra is calling +254712345678...  
Brand: Asus, Model: ROG Phone 6, Storage: 256GB  
Asus ROG Phone 6 with Adreno 730 is playing eFOOTBALL!

---
#  Activity 2: Vehicle Polymorphism in Python  

---

##  File Structure  
polymophism.py

# Base class

---

## Code Implementation  

```python
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing on water...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Polymorphic behavior
```
# Expected Output
 Driving on the road...  
 Flying in the sky...  
 Sailing on water...

