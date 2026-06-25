# Fourth Example - introduces match

name: str = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # the pipe is OR
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Third Example - introduces match

# name: str = input("What's your name? ")
# 
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

# the underscore is a special character that means 'anything else' in match


# Second Example

# name: str = input("What's your name? ")
# 
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


# First Example

# name: str = input("What's your name? ")
# 
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

