from random import randint, choice
from datetime import datetime, timedelta, date

# This is a Car Rental Implementation
class Car(object):
    def __init__(self, make: str, model: str, year: int, available: int):
        self.make = make
        self.model = model
        self.year = year
        self.total_cars = available
        self.available_to_rent = available
        self.car_borrowed_by = {}
        self.cost_per_day = randint(20, 150)

    def __str__(self):
        return f"Car: {self.make}, {self.model} from the year {self.year}"


class Person(object):
    def __init__(self, name: str, role: str):
        self.name = name
        self.id = randint(0, 100) # Id given when creating a user
        self.role = role # Admin, Guest, Member

    def get_id(self):
        return self.id

    def __str__(self):
        return f"Name: {self.name} Id: {self.id} and has the Role: {self.role}"

class Member(Person):
    def __init__(self, name, email, role):
        super().__init__(name, role)
        self.memberId = f"{choice(["WE", "TS", "ZR","AK"])}{randint(100, 999)}{choice(["FGW", "L3K", "I0D", "78G"])}"
        self.email = email
        self.car_borrowed = [] # Will show the car make
        self.return_by = {} # Will show the date for { make: return_date }
        self.rental_cost = {} # Will show the cost incurred cost_per_day * numbers_of_days
        self.history = {} # List of all rentals in the year ()
        self.points_collected = 0 # Calculated by (number_of_rentals * 0.05 * 100)/12

    def calculate_points(self, current_year: int):
        if len(self.history[current_year]) > 0:
            self.points_collected = (len(self.history[current_year]) * 0.05 * 100)/12
        else:
            return f"Member: {self.id} has not collected points yet."

    def __str__(self):
        return f"Name: {self.name}\nRole: {self.role}\nCar borrowed: {self.car_borrowed[self.id]}\nPoints Earned: {self.points_collected}"


class Guest(Person):
    def __init__(self, name, email, role):
        super().__init__(name, role)
        self.email = email


class CarRentalCompany(object):
    def __init__(self):
        self.cars = {}
        self.members = {}
        self.minimum_days = 1 # 1 Day is around 24 hours calculated later using datetime
        self.current_rentals = []

    def add_car(self, make, model, year, available=1):
        self.cars[make] = Car(make, model, year, available)
        print(f"{self.cars[make]}")

    def add_member(self, name, email, role):
        new_member = Member(name, email, role)
        if new_member.memberId not in self.members:
            self.members[new_member.memberId] = new_member
        return f"{new_member.memberId} already a member!"

    def get_car(self, car_make):
        return self.cars[car_make]

    def get_member(self, memberId):
        return self.members[memberId]

    def add_guest_to_members(self, other):
        self.add_member(other.name, other.email, "Member")

    def rent_car(self, memberId, car_make, days):
        if memberId not in self.members:
            return "Sorry! Can't rent a car unless a Member."
        if car_make not in self.cars:
            return "Sorry! Car not in the list"

        car = self.cars[car_make]
        member = self.members[memberId]
        if memberId in self.current_rentals:
            return "Sorry! You can only rent one car."
        if car.available_to_rent <= 0:
            return "Sorry! Car is currently booked.\nLook at other options."

        car.available_to_rent -= 1
        member.car_borrowed.append(car_make)
        due_date = datetime.now + timedelta(days=days)
        member.return_by[car_make] = due_date
        member.rental_cost[car_make] = f"${(car.cost_per_day * days * 1.02)}"
        car.car_borrowed_by[memberId] = due_date
        self.current_rentals.append(car)
        if date.year not in member.history:
            member.history[date.year] = []
        else:
            member.history[date.year].append(car_make)

    def display_status(self):
        print("="*20)
        print("Welcome to the Rental Spot")
        print("="*20)
        print(f"Registered Cars: {len(self.cars.items())}")
        for car in self.cars:
            print(car)
        print(f"Registered Members: {len(self.members.items())}")
        for member in self.members:
            print(member)



if __name__ == "__main__":
    guest_user = Guest("William", "william@myaccount.com", "Guest")
    # Add cars and members to the Rental Spot
    enterprise_rental = CarRentalCompany()
    enterprise_rental.add_member("James", "james@gmail.com", "Member")
    enterprise_rental.add_member("Fred", "fred.12@yahoo.com", "Member")
    enterprise_rental.add_car("Honda", "Civic", 2024, 10)
    enterprise_rental.add_car("Mercedes", "Benz AMG", 2020, 4)
    enterprise_rental.add_car("Toyota", "Supra", 2021, 6)
    enterprise_rental.add_car("Genesis", "GS40 RS", 2022)
    # Create a rental
    enterprise_rental.display_status()