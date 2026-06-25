# Thirteenth Example

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
    # this is also a pattern
    #   if n > 0:
    #       break
    # return n
    # 
    # return of a value actually hands back a value that the caller can use in other areas of code

def meow(n):
    for _ in range(n):
        print("meow")

main()

# Twelfth Example - introduce a meow function

# def main():
#     meow(3)
# 
# def meow(n):
#     for _ in range(n):
#         print("meow")
# 
# main()

# Eleventh Example - this removes the else; saying wait until the user gives a value of more than zero keep prompting
# common paradigm in python to present to a user that you want them to enter a specific value

# while True:
#     # ask the user for input
#     n = int(input("What's n? "))
#     if n > 0: # this checks to make sure the user puts in a number greater than 0
#         break
# 
# # once the while loop breaks then print meow for the number of times in n
# # if n = 3 then meow will appear 3 times in the terminal
# for _ in range(n): 
#     print("meow")

# reminder: underscore is a pythonic way to indicate a variable is needed for the keyword but the name of
# the variable doesn't need to be understood by a human reader of this code

# Tenth Example - introduce the while True: use caution while True: can throw an infinite loop 
# ctrl + c to break out if this happens while writing code before the structure to stop is in place

# while True:
#     # ask the user for input
#     n = int(input("What's n? "))
#     if n < 0:
#         continue # built in keyword
#     else:
#         break # built in keyword


# Ninth Example - another way to do a loop but if this makes code difficult for others; maybe not appropriate

# print("meow\n" * 3, end="")

# this is totally pythonic way to do this
# the end="" is a call back to lecture 0

# Eigth Example - look at the underscore where the i used to be

# for _ in range(3):
#     print("meow")

# points out that i is never used and there is a pythonic way to do this
# an underscore can be used within Python to show that the variable is just required
# but the human doesn't need to use it or to have a name to explain it
# you do not care what the name is... so no need to create one.

# Seventh Example - introduce new function range that is built into Python

# for i in range(3):
#     print("meow")

# values start at 0 and up to the number passed into the function
# range(10000000) would be the way to count to one million

# Sixth Example - introduce new keyword for

# for i in [0, 1, 2]:
#     print("meow")

# this is poorly designed... think what it would be like if you needed to do this one million times

# Fifth Example - different way to increment count

# i: int = 0
# 
# while i < 3:
#     print("meow")
#     i += 1 # special operator += short hand for adding a value to count i

# Fourth Example - increment the count i and start count i at 0

# i: int = 0
# 
# while i < 3: # operator change to less than
#     print("meow")
#     i = i + 1

# Third Example - increment the count i

# i: int = 1
# 
# while i <= 3: # operator change to less than or equal to
#     print("meow")
#     i = i + 1

# by CS convention counting typically starts at 0 to cover other data types and patterns 

# Second Example - decrement the count i

# i: int = 3
# 
# while i != 0: # operator is not equal to
#     print("meow")
#     i = i - 1


# introducing the while loop
# ctrl + c in terminal will end an infinite loop situation

# First Example

# print("meow")
# print("meow")
# print("meow")
