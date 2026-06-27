# Fifth Example - introduce the walrus operator

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # := this is to assign and if or elif on the same line
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# this is a more compact form
# walrus operator is new to the Python language
# may not be in older versions that I work with

# Fourth Example

# import re
# 
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name) # (.+) group(1) (.+) group(2); also * added to handle 0 or more than 1 space in front of group(2)
# 
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")


# Third Example

# import re
# 
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name) # using the variable to see what's matching
# 
# # the parenthesis (.+) is used for capturing purposes
# 
# if matches:
#     last, first = matches.groups() # returns all of the groups that were captured
#     name = f"{first} {last}"
# print(f"hello, {name}")

# Second Example

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")
# 
# # problems with this code at the .split
# # what if the user doesn't use a comma space?


# First Example - let's format a user's name after they input

# name = input("What's your name? ").strip() # .strip removes whitespace
# print(f"hello, {name}")

# this just introduces the problem to be worked out during the demo