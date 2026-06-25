# Seventh Example - introduce list of dictionaries and the None special keyword

# creating a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Sixth Example

# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# 
# for student in students:
#     print(student, students[student], sep=", ")
# 
# # this syntax students[student] returns the value
# # student in square brackets is the same as using i in other for loop examples
# # sep=", " is a call back to lecture_0

# Fifth Example - introduce using the for keyword on dict data type

# # "key": "value"
# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# 
# for student in students:
#     print(student)
# 
# # dict data type in for outputs the key
# # knowing to use the key as a way to access the value is useful look at Sixth Example

# Fourth Example - introduce the dict data type

# "key": "value"
# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# 
# # pass the key and get the value
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# Third Example - if you need to use numbers - introduce function len

# students: list = ["Hermione", "Harry", "Ron"]
# 
# for i in range(len(students)):
#     print(i + 1, students[i])

# len is a built in function

# Second Example - introduce for keyword can iterate over anything including strings

# students: list = ["Hermione", "Harry", "Ron"]
# 
# for student in students:
#     print(student)

# this allows me to not know in advance the number of items in the list
# student is used in the print statement because it's important if a human reads code
# underscore could be used "technically" but it would obscure meaning for human code reader

# First Example

# students: list = ["Hermione", "Harry", "Ron"] # I added the type hint : list
# 
# print(students[0])
# print(students[1])
# print(students[2])

# lists in Python are zero indexed