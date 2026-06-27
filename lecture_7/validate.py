# Fifteenth Example - looking at the characters prior to @

import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # another way to allow multiple words separated by . in username
    print("Valid") 
else:
    print("Invalid")

# still not code that allows to cover all possible test cases
# re.match
# re.fullmatch
# are also available in the library

# Fourteenth Example - grouping to handle subdomains

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # tolerate a subdomain that may or may not be in user input
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # let's handle the different domains
# # use the group operator
# # (\w+\.)? the pattern in parenthesis can be there 0 or more than 1 times and the ? allows this to be optional
# # this handles the cases where there are one or more subdomains in the email address


# Thirteenth Example - introduce flags of re library 

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): # using the re.IGNORECASE
#     print("Valid") 
# else:
#     print("Invalid")
# 
# there is still an issue with valid email address
# % python3 validate.py
# What's your email? joseph@my.email.edu
# Invalid
# 
# 
# # if user passes in a .EDU the pattern has to know this is okay
# 
# # flags can be used to configure the re.search()
# # re.IGNORECASE
# # re.MULTILINE
# # re.DOTALL
# 
# # group example (\w|\s) the pipe is an OR
# 
# # additional RegEx Syntax
# # A|B either A or B
# # (...) a group
# # (?:...) non-capturing version


# Twelfth Example - this is a far more restrictive pattern to limit unacceptable input values

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^\w+@\w+\.edu$", email): # removed the long [a-zA-Z0-9_] replaced with built in \w
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # there are some built in patterns that can be used
# # \w is any word including numbers and underscore
# 
# # additional special characters for RegEx
# # \d decimal digit 0-9
# # \D not a decimal digit (anything not 0-9)
# # \s whitespace characters
# # \S not a whitespace character
# # \w word character ... as well as numbers and the underscore
# # \W not a word character


# Eleventh Example - this is a far more restrictive pattern to limit unacceptable input values

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # focus RegEx on only these are acceptable characters
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # What are characters I want to limit as acceptable
# # [a-z] this is a range of characters for lowercase letters
# # [A-Z] this is a range of characters for uppercase letters
# # [0-9] this is a range of numbers 
# # [_] underscore is included in acceptable
# #
# # these ranges can be combined together

# Tenth Example - introduce [] and [^] special symbols

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^[^@]+@[^@]+\.edu$", email): # [^@] means any character except the @ symbol
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # there is still an issue with the Ninth Example
# # 
# # Ninth Example allows multiple @ symbols that Tenth Example fixes
# # % python3 validate.py
# # What's your email? joseph@@@email.edu
# # Valid
# 
# # additional special characters for Regex
# # [] set of characters
# # [^] complementing the set
# 
# # with the addition of [^@] in place of the . the code now marks multiple @ symbols as invalid
# # 
# # % python3 validate.py
# # What's your email? joseph@@@email.edu
# # Invalid
# # code still isn't completely covering all the possible test cases


# Ninth Example - additional symbols to use in RegEx to fine tune pattern

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r"^.+@.+\.edu$", email): # special symbols to control the length of the pattern matching
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # additional symbols to learn
# # ^ matches the start of the string
# # $ matches the end of the string or just before the newline at the end of the string
# 
# # this code works for these different test cases
# # % python3 validate.py
# # What's your email? this is email joseph@email.edu
# # Valid
# # 
# # % python3 validate.py
# # What's your email? joseph@email.edu
# # Valid


# Eighth Example - introduce r string; \ special sequence in RegEx for literal character

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(r".+@.+\.edu", email): # r is the 'raw string' - \ is a special sequence - here this means that it matches only the .
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # good habit to just use the r" string for all regex in Python

# # % python3 validate.py
# # What's your email? booth@email?edu
# # Invalid


# Seventh Example - introduce 'finite state machine'

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(".+@.+.edu", email): # added .edu in argument
#     print("Valid") 
# else:
#     print("Invalid")
# 
# # this code is still not quite to where it needs to be
# # the . before edu is interpretted as 'any characters except a newline'
# 
# # % python3 validate.py
# # What's your email? booth@email?edu
# # Valid
# 
# # non-deterministic finite automaton
# # . any characters except a newline
# # * 0 or more repetitions
# # + 1 or more repetitions
# # ? 0 or 1 repetitions
# # {m} m repetitions
# # {m,n} m-n repetitions
# 
# # ```mermaid
# # flowchart LR
# #     A([Start])
# #     B["Consume characters<br/>.*"]
# #     C["Find '@'"]
# #     D["Consume remaining characters<br/>.*"]
# #     E([Match])
# # 
# #     A --> B
# #     B -->|not @| B
# #     B -->|@| C
# #     C --> D
# #     D -->|any character| D
# #     D -->|EOF| E
# # ```


# Seventh Example - introduce search function

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(".+@.+", email): # changed from * to +
#     print("Valid")
# else:
#     print("Invalid")
# 
# # .* allows for 0 repetitions

# Sixth Example - introduce search function

# import re
# 
# email = input("What's your email? ").strip()
# 
# if re.search(".*@.*", email):
#     print("Valid")
# else:
#     print("Invalid")
# 
# # RegEx has more powerful special symbols for expressing a pattern
# # this is a useful library and is used across many programming languages
# # . any characters except a newline
# # * 0 or more repetitions
# # + 1 or more repetitions
# # ? 0 or 1 repetitions
# # {m} m repetitions
# # {m,n} m-n repetitions


# Fifth Example

# import re # included with Python
# 
# email = input("What's your email? ").strip()
# 
# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")
# 
# # this is just a tip-toe into using the library
# # not much of an improvement over previous examples


# Fourth Example - new string function 'endswith'

# email = input("What's your email? ").strip()
# 
# username, domain = email.split("@")
# 
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
# 
# # still does not fully fix the issue
# # this demo shows how complex this path gets for this type of solution pattern
# # these examples lead into the RegEx part of the course
# # RegEx allows for pattern matching of a string
# # re is a library that provides this functionality
# # https://docs.python.org/3.14/library/re.html
# # re.search(pattern, string, flags=0)

# Third Example - introduce the split method on string argument

# email = input("What's your email? ").strip() # strip removes whitespace to the left and right of string
# 
# username, domain = email.split("@") # reminder - called 'unpacking' by assigning return values from a function to two variables in one line
# 
# if username and "." in domain: # turns out if there is even one character in this variable return is True
#     print("Valid")
# else:
#     print("Invalid")
# 
# # starting to get a bit better but not ideal


# Second Example

# email = input("What's your email? ").strip() # strip removes whitespace to the left and right of string
# 
# if "@" in email and "." in email: # now we're also checking for period in string
#     print("Valid")
# else:
#     print("Invalid")
# 
# # still problems with this code

# First Example

# email = input("What's your email? ").strip() # strip removes whitespace to the left and right of string
# 
# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")
# 
# # problem with this code because any string with any number of @ characters is "Valid"

