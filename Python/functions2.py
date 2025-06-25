# deep dive into functions
# nested functions

# def outer_function():
#     def inner_function():
#         # code
#     return inner_function

def outer():
    def inner():
        return "This is the innner function!"
    return inner()

# print(outer())
# print(inner())

def process_data(data: list):
    def clean(d):
        return d.strip().lower()
    return [clean(item) for item in data]

# print(process_data([" Hello ", "WORLD   "]))

def power_of(n):
    def power(x):
        return x**n
    return power

square_root = power_of(2)
cube_root = power_of(3)


print(square_root(10))
print(cube_root(2))
