# Eleventh Example

def f(*args, **kwargs):
    print("Named: ", kwargs)

f(galleons=100, sickles=50, knuts=25)

# *args and **kwargs allows support for variable numbers of arguments
# the key here are the * and **
# I do not have to call the variable arguments as args
# I do not have to call the variable keyword arguments as kwargs
# when reading documentation like in print()
# there is print(*object) is just saying the print function accepts multiple arguments

# Tenth Example - looking at **kwargs

# def f(*args, **kwargs):
#     print("Named: ", kwargs)
# 
# f(galleons=100, sickles=50, knuts=25)
# 
# # kwargs is automatically a dictionary


# Ninth Example - introduce *args **kwargs

# def f(*args, **kwargs):
#     print("Positional: ", args)
# 
# f(100, 50, 25, 5) # added a fourth argument and no error in program

# Eighth Example - introduce *args **kwargs

# def f(*args, **kwargs):
#     print("Positional: ", args)
# 
# f(100, 50, 25)
# 
# # *args some number of positional arguments
# # **kwargs some number of keyword arguments


# Seventh Example - unpack dictionary

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# 
# print(total(**coins), "Knuts") # added ** to coins
# 
# # the keys and values are passed into the total function
# # **coins is similar to this syntax galleons=100, sickles=50, knuts=25
# # very cool

# Sixth Example

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# 
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# 
# # this is valid but imagine that the dictionary is much larger


# Fifth Example

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# this works - setup for demo the dict data type

# Fourth Example - unpacking a list

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# coins = [100, 50, 25]
# print(total(*coins), "Knuts") # the * in front of coins - this is powerful
# 
# # *coins unpacks the individual values in the indexes
# # unpacks the data structure

# Third Example

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "Knuts")


# Second Example

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# 
# print(total(100, 50, 25), "Knuts")


# First Example

# first, last = input("What's your name? ").split(" ")
# print(f"hello, {first}")


