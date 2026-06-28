# Second Example - introduce set data type

# list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# swap to a set() for this demo
houses = set()

for student in students:
    houses.add(student["house"]) # notice the method add 

for house in sorted(houses):
    print(house)


# First Example

# # list of dictionaries
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
# 
# # created a list to accumulate
# houses = []
# # loop through the students dictionary to get house
# # add house to houses list if not in houses list already
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
# # print the items in the houses list
# for house in sorted(houses):
#     print(house)
# 
# # this is the demo on one way to do this type of work
