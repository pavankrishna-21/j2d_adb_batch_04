class Animal: # base class | parent class
    def speak(self):
        return "Animal Speaks"

class Cat(Animal): # derived class | child class
    def get_cat_details(self):
        return "Cat name is Bruno"
    
class Dog(Animal):
    def get_dog_details(self):
        return "Dog name is Frank"
    
# my_dog = Dog()
# print(my_dog.speak())


class GrandParent():
    def grand_parent_func(self):
        return "I'm the grand parent"

class Parent(GrandParent):
    def parent_func(self):
        return "I'm the parent"

class Child(Parent):
    def child_func(self):
        return "I'm the child"
    
# my_child = Child()
# print(my_child.parent_func())
# print(my_child.grand_parent_func())
# print(my_child.child_func())


class ParentMother():
    def parent_mother_func(self):
        return "I'm the mother parent"

class ParentFather():
    def parent_father_func(self):
        return "I'm the father parent"

class Child(ParentFather, ParentMother):
    def child_func(self):
        return "I'm the child"
    
my_child = Child()
print(my_child.parent_father_func())
print(my_child.parent_mother_func())
print(my_child.child_func())
