# Fifth Example - introduce slice 

import sys 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)    

# the [1:] is the slice of the list
# starts at element 1 and goes all the way through all elements
# % python3 name.py joseph justin ellie mackenzie
# hello, my name is  joseph
# hello, my name is  justin
# hello, my name is  ellie
# hello, my name is  mackenzie
# a smaller slice can be identified with [1:3] for example
# negative numbers can be used to remove items from the slice
# example [1:-1]

# Fourth Example

# import sys 
# 
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# 
# for arg in sys.argv:
#     print("hello, my name is ", arg)    
# 
# # sys.argv is a list so the for loop can be used
# # this version has a small error where all indexes are
# # printed to the console
# # value at index 0 is the file name
# # recall that the user is passing in arguments when running the program
# # python3 name.py joseph justin ellie mackenzie
# # hello, my name is  name.py
# # hello, my name is  joseph
# # hello, my name is  justin
# # hello, my name is  ellie
# # hello, my name is  mackenzie

# Fourth Example - introduce sys.exit

# import sys 
# 
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# 
# print("hello, my name is", sys.argv[1])
# 
# # sys.exit helps filter out the errors without running 
# # sys.exit exits from the program itself the user has to call the program from command line each time
# # sys.exit is being used to protect the user from hitting
# # print("hello, my name is", sys.argv[1]) blindly and throwing an error
# # remember python executes from top to bottom so print statement
# # is only run if there are the right number of arguments

# Third Example - defensive posture for writing code

# import sys 
# 
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])
# 
# # conditionals allow for more specific error messages
# # this allows for checking before an error is thrown
# # more proactive approach to writing code

# Second Example

# import sys 
# 
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# common error thrown if the command line input does not contain a
# value in index 1 IndexError
# example % python3 name.py 
# because sys.argv[1] has no value - an error appears in console
# the try: except: block helps handle the issue

# First Example - introduce sys library and argv function

# import sys 
# 
# print("hello, my name is", sys.argv[1])

# https://docs.python.org/3.14/library/sys.html
# sys.argv is a list
# sys.argv allows for passing an argument when running the file from command line
# example % python3 name.py Joseph
# sys.argv[0] is name.py