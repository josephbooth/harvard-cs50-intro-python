# Ask user for their name; use str.methods strip and title to clean up whitespace and capitalize first chars
name: str = input("What's your name? ").strip().title()

# demo'd this in course first, last = name.split(" ") 

# Say hello to user
print(f"hello, {name}") # this uses an f string

# looking at the name variable - : str - is called a type hint (not in the video) I learned this recently from a different source
# added the type hint as a way to keep practicing this idea... hopefully will become a habit

# input() is a Python function to get input from a user

# also valid:
# print("hello, " + name)
# print("hello ", name)

# print() is a pre-built function provided by Python
# an arugument is an input to a function
# print() allows for arguments to be passed by separating with a comma
# example: print("hello ", name) this is two arguments

# docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# everything in the parenthesis are parameters - potential arguments
# *objects means any number of objects can be passed in
# sep=' ' this is the default for the amount of space added between arguments
# end='\n' this is the default of the function; this can be modified by passing in a different value for end
# sep and end are called "Named Parameters"

# escape characters use a backslash so that literal characters can appear in strings
# example print("hello \"friend\"")

# docs.python.org/3/library/stdtypes.html#string-methods
## str.strip(chars=None, /)

# '   spacious   '.strip() <- no arguments - then whitespace from leading and trailing characters
# 'spacious'

# 'www.example.com'.strip('cmowz.') <- argument supplied
# 'example'

# comment_string = '#....... Section 3.2.1 Issue #32 .......'
# comment_string.strip('.#! ')
# 'Section 3.2.1 Issue #32'

# https://docs.python.org/3/library/stdtypes.html#str.title
## str.title()

# 'Hello world'.title()
# 'Hello World'

