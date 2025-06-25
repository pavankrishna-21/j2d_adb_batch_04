# loops 

# 1. for loops 
# 2. while loops

# li = ["Orange", "Banana", "Pineapple"]
# for i in li:
#     print(i)

# range() -> create sequence of numbers to iter

# for i in range(1, 11, 3):
#     print(i)
    
# for i in range(0, 11, 1):
#     print(i)
    
# for ch in "jagadesh":
#     print(ch)

# name = input("Enter the Name: ")
# # find the no.of vowels in the name
# vowels = ['a', 'e', 'i', 'o', 'u']

# vowel_count = 0
# for ch in name:
#     if ch in vowels:
#         vowel_count += 1
        
# print("There are", vowel_count, "vowels in", name)

# while condition:
#     code 

# c = 0
# while c <= 5:
#     print(c)
#     c+=1
    

# while True:
#     resp = input("Type 'Exit' to stop: ")
#     if resp == "Exit":
#         break
#     else:
#         print("Your response: ", resp)
        
        
# for i in range(1, 6):
#     if i == 3:
#         continue
#     else:
#         print(i)


# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# .
# .
# .
# 2* 10 = 20

# for i in range(1, 11):
#     print("2 *", i, "=", 2*i)
    
# string formaters

# 1. .format()

# for i in range(1, 11):
#     print("2 * {iter} = {mul}".format(iter=i, mul=2*i))
    
# # 2. f""
# for i in range(1, 11):
#     print(f"2 * {i} = {2*i}")

# for i in range():
#     for j in range():

# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# .
# .
# .
# 2* 10 = 20

# 3 * 1 = 2
# 3 * 2 = 6
# 3 * 3 = 9
# .
# .
# .
# 3 * 10 = 30

# for i in range(2, 6):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("---------------------------------")


# for i in range(6, 0, -1):
#     print(i * "*")