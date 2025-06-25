from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass 
        # you should not implement anything in abc 

class Car(Vehicle):
    
    def get_car_details(self):
        return "This is Toyota Fortunier"
    
    def move(self):
        return "This car move at top 160 KMPH"
    
class Bike(Vehicle):
    def get_bike_details(self):
        return "This is Hybusa"
    
    def move(self):
        return "This bike moves at top 320 KMPH"
    
my_car = Car()
print(my_car.get_car_details())


my_bike = Bike()
print(my_bike.get_bike_details())
