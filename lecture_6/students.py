# Fourteenth Example

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students-write-to.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # these are the headers in the csv file
    writer.writerow({"name": name, "home": home})



# Thirteenth Example

# import csv
# 
# name = input("What's your name? ")
# home = input("Where's your home? ")
# 
# with open("students-write-to.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])
# 
# # csv writer handles quotes and newline


# Twelfth Example - csv with a header row

# import csv
# 
# students = []
# 
# with open("students-header-row.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
# 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# 
# # created a students-header-row.csv file for this demo
# # this method... using the DictReader it helps combat against changes in the csv

# Eleventh Example - introduce the csv library

# import csv
# 
# students = []
# 
# with open("students-home.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})
# 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# 
# # https://docs.python.org/3.14/library/csv.html
# # I'm getting a ValueError with this current version of code
# # the demo did not throw this error
# 
# # % python3 students.py
# # Traceback (most recent call last):
# #   File "harvard-cs50-intro-python/lecture_6/students.py", line 9, in <module>
# #     for name, home in reader:
# #         ^^^^^^^^^^
# # ValueError: too many values to unpack (expected 2, got 3)
# 
# # went back to rewatch the section and there was a moment where the instructor
# # added quotes around the second value in the Harry,"Number Four, Privet Drive" line
# # code now executes correctly
# 
# # the csv library figured out the commas and quotes automatically


# Tenth Example

# students = []
# 
# with open("students-home.csv") as file:
#     for line in file:
#         name, home  = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student) 
# 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# 
# # the code has an error at this point due to the file using csv
# # and we're splitting on the comma which is making three values in the .split line
# # deviated from the video and created a new file student-home.csv
# # so that the other example code will still work later on down the road

# Ninth Example

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student) 
# 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")
# 
# # lambda student: student["name"])
# # this is an anonymous function
# # not completely following this


# Eighth Example - sort by house

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student) 
# 
# def get_house(student):
#     return student["house"]
# 
# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")
# 
# # sorted by house in reverse order

# Seventh Example - reverse the sort

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student) 
# 
# def get_name(student):
#     return student["name"]
# 
# for student in sorted(students, key=get_name, reverse=True): # named parameter reverse=True to Z-A output
#     print(f"{student['name']} is in {student['house']}")
# 
# # this sorts students by name using get_name function

# Sixth Example - how to sort when using a list of dictionaries

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} # notice the syntax difference from fourth example 
#         students.append(student) 
# 
# def get_name(student):
#     return student["name"]
# 
# for student in sorted(students, key=get_name): # passing a function as an argument
#     print(f"{student['name']} is in {student['house']}")
# 
# # we telling python to sort this list by looking at this key in each dictionary
# # we can tell sorted function to use named parameter called key


# Fifth Example - dict syntax demo

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} # notice the syntax difference from fourth example 
#         students.append(student) 
# 
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
# 
# # the dictionary syntax is much shorter here

# Fourth Example - demo better way to sort on the students themselves, use a dictionary

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {} # create empty dictionary
#         student["name"] = name # for key name add value stored in name variable
#         student["house"] = house # for key house add value stored in house variable
#         students.append(student) # append this student to the students list
# 
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
# 
# # this is working code... a bit verbose according to instructor
# # does not yet sort the students

# Third Example - demo sort

# students = []
# 
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}") # the idea here is to accumulate sentences in a list to apply sort function
# 
# for student in sorted(students):
#     print(student)
# # this code is sorting the entire sentence in the list; not by the students name solely


# Second Example

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # notice there are two variables
#         print(f"{name} is in {house}")
# 
# # demos how to unpack the list into two variables
# # python technique


# First Example - read a .csv file, introduce split function available on all strings in python

# with open("students.csv") as file:
#     for line in file:
#         row: list = line.rstrip().split(",") # row is a common paradigm to keep in mind
#         print(f"{row[0]} is in {row[1]}") # row is a list that can be accessed by index
# 
# # I added the type hint

