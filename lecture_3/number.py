# Eleventh Example

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

main()

# this is more reusable code form with the parameters

# Tenth Example - introduce keyword pass

# def main():
#     x = get_int()
#     print(f"x is {x}")
# 
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             pass
# 
# main()
# 
# # it sounds like python is designed to encourage the use of try statements
# # versus using if elsif etc.

# Ninth Example
# def main():
#     x = get_int()
#     print(f"x is {x}")
# 
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             print("x is not an integer")
# 
# main()

# Eighth Example - while loop and try within a function
# def main():
#     x = get_int()
#     print(f"x is {x}")
# 
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x
# 
# main()
# 
# # return will break out of this loop as it does both it's considered stronger than just break as seen in Seventh Example

# Seventh Example - while loop and try within a function
# def main():
#     x = get_int()
#     print(f"x is {x}")
# 
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x
# 
# main()

# Sixth Example - in response to student question
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"x is {x}")
# 
# # without the break in the else this code never stops running
# # must use the break for the while loop        

# Fifth Example - use a loop with try
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# 
# print(f"x is {x}")

# Fourth Example

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# Third Example

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")


# Second Example - introduce keyword try - allows to check if something went wrong

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")
# 
# # ValueError appeared in the error message from 'cat'

# First Example

# x = int(input("What's x? "))
# print(f"x is {x}")

# try entering the word 'cat' as an input
