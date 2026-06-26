# Eleventh Example - introduce the reverse parameter in the sorted function

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True): # notice the reverse=True by default this is set to False
    print(f"hello, {name}")

# https://docs.python.org/3.14/library/functions.html#sorted
# sorted(iterable, /, *, key=None, reverse=False)

# Tenth Example - sort on the file contents themselves

# with open("names.txt") as file:
#     for line in sorted(file):
#         print(f"hello,", line.rstrip())
# 
# # demo'd to show that this can become very compact

# Ninth Example - introduce the sort output of file contents

# names = []
# 
# # the r argument is the default for the function
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip()) # remember names is a list that lives in memory
# 
# # sorted happens before the loop starts
# for name in sorted(names):
#     print(f"hello, {name}")
# 
# # sort has to be done before outputting the contents of file


# Eighth Example - demo the for loop as a part of with

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())
# 
# # this is a pythonic way to do the same work as the Seventh Example
# # more compact


# Seventh Example - introduce rstrip function

# with open("names.txt", "r") as file:
#     lines = file.readlines()
# 
# for line in lines:
#     print("hello,", line.rstrip()) # rstrip removes the newline character
# 
# # fixes the extra newline character in the console output

# Sixth Example - read from the file, introduce readlines method

# # notice the argument is now r
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# 
# for line in lines:
#     print("hello,", line)
# 
# # this version of the code has an extra \n in the output

# Fifth Example - pythonic way to manipulate files, keyword with

# name = input("What's your name? ")
# 
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# 
# # notice that the file.close() statement is no longer required
# # this method automatically closes the file

# Fourth Example - fix the missing line return so the names in the file are one on top of the other

# name = input("What's your name? ")
# 
# file = open("names.txt", "a") # a argument signals append to file
# file.write(f"{name}\n") # added the f string with a line return \n
# file.close()

# Third Example - introduce append argument 

# name = input("What's your name? ")
# 
# file = open("names.txt", "a") # a argument signals append to file
# file.write(name)
# file.close()
# 
# # this code fixes the overwrite issue found in Second Example
# # the change happened in the second argument of open function
# # introduces a different issue where all the names are written to a single line
# # in the file


# Second Example - introduce function open and w write argument

# name = input("What's your name? ")
# 
# file = open("names.txt", "w") # w argument signals write to file
# file.write(name)
# file.close()
# 
# # open is a programmers technique
# # https://docs.python.org/3.14/library/functions.html#open
# # there is an error in this code... it recreates the names.txt file
# # every time it runs which is overwriting the previous version


# First Example - introduce the empty list, append method, sorted function

# names = []
# 
# for _ in range(3):
#     names.append(input("What's your name? "))
# 
# for name in sorted(names):
#     print(f"hello, {name}")
# 
# # code in this state outputs as
# # % python3 names.py
# # What's your name? Ron
# # What's your name? Hermione
# # What's your name? Harry
# # hello, Harry
# # hello, Hermione
# # hello, Ron
# 
# # the list data only lives for the time the program is running
