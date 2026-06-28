# Fifth Example - introduce enumerate

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)


# Fourth Example - dictionary comprehensions

# students = ["Hermione", "Harry", "Ron"]
# 
# gryffindors = {student: "Gryffindor" for student in students} # dictionary comprehension
# 
# print(gryffindors)
# 
# # this makes a single dictionary


# Fourth Example - list comprehensions

# students = ["Hermione", "Harry", "Ron"]
# 
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students] # list comprehension
# 
# print(gryffindors)


# Third Example - setup of the non-dictionary comprehension

# students = ["Hermione", "Harry", "Ron"]
# 
# gryffindors = []
# 
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
# 
# print(gryffindors)


# Second Example - introduce filter function

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# 
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
# 
# gryffindors = filter(is_gryffindor, students) # pass in function first and then what object to filter
# 
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): # sorting a dict requires a key argument
#     print(gryffindor["name"])
# 
# # lambda as the key is still a bit confusing...
# # this is something to spend some time on in the future.


# First Example - list comprehension with a conditional

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# 
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor" # list comprehension conditional
# ]
# 
# for gryffindor in sorted(gryffindors):
#     print(gryffindor) 