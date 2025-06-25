# functions

# def greet():
#     return "Hello World"

# print(greet())
# print(greet())

def addition(a, b):
    return a + b

# print(addition(10, 20))
# print(addition(100, 40))
# print(addition(300, 400))

def square(n):
    return n**2

# print(square(4))

# def addition(a, b, c=0):
#     return a + b + c

# print(addition(a=10, b=30))
# print(addition(a=10, b=30, c=40))


# def addition(*args):
#     return sum(args)

# print(addition(10, 20, 30, 40, 50, 60, 5, 6, 7, 8, 9))


# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# print(print_info(name="Jagadesh", age=35, occupation="Tech"))

# variable scope

x = 10 # Global Variable

def some():
    c = 5 # local variable
    return c


print(x)
print(some())
    