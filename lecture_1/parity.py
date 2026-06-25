# Fourth Example

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0 # the idea is to get to the bool return built into the data type the == creates a True False evaluation
    
main()


# Third Example

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# 
# def is_even(n):
#     return True if n % 2 == 0 else False # remove the zero and code still runs - editor show red squiggles
    
# main()

# Second Example

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# 
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#     
# main()

# boolean data type introduced
# MUST be written capital T True and capital F False

# First Example

# x = int(input("What's x? "))
# 
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd") 
