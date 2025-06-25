from datetime import datetime

# class Dog:
#     def tommy(self):
#         return "bow bow.. this is tommy"

# my_dog_tommy = Dog()
# print(my_dog_tommy.tommy())

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
            
#     def get_dog_details(self):
#         return f"bow bow.. this is {self.name} and I'm a {self.breed}"

# my_dog = Dog(name="Bruno", breed="Doberman")
# print(my_dog.get_dog_details())

# my_dog2 = Dog(name="Frank", breed="Husky")
# print(my_dog2.get_dog_details())


# class Person():
#     population = 0
    
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
    
#     @classmethod
#     def total_population(cls):
#         return cls.population
    
# p1 = Person("Ravi")
# print(p1.total_population())
# print(Person.total_population())


# class Person():
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         current_year = datetime.now().year
#         return cls(name, current_year-birth_year)

# p = Person.from_birth_year("Ravi", 1996)
# print(p.name, p.age)

# class Math():
#     @staticmethod
#     def add(x, y):
#         return x + y


# print(Math.add(10, 30))