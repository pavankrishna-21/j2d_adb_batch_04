# oops

# inheritance

class Animal:  # parent class | base class
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):  # child class | derived class
    def bark(self):
        return "Dog barks"

my_dog = Dog()
print(my_dog.speak())
print(my_dog.bark())