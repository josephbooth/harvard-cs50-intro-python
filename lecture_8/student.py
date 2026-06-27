# Tenth Example 

class Student:  
    def __init__(self, name, house): # 
        self.name = self.name
        self.house = self.house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # 
    return student

if __name__ == "__main__":
    main()



# Ninth Example - classes are mutable, they come with methods

# class Student:  
#     def __init__(self, name, house): # this is called when creating an object from this class
#         self.name = self.name
#         self.house = self.house
# 
# # what is self?
# # convention is to always call it self - could technically be any name
# # self is the memory location of the created instance of the object
# 
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house) # Student(name, house) considered a construtor or instantiate object
#     return student
# 
# if __name__ == "__main__":
#     main()


# Ninth Example - introduce class keyword

# # capital S in Student is a common convention
# class Student:  # keyword included with python ... is a valid placeholder too
#     ...
# 
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}") # accessing the contents of the 
# 
# def get_student():
#     student = Student() # created a Student
#     student.name = input("Name: ") # .name and .house are called attributes
#     student.house = input("House :")
#     return student
# 
# if __name__ == "__main__":
#     main()
# 
# # Python provides a way to create our own data types
# # this is called a class - a blueprint or mold for a type of data
# # classes allow the programmer to create a custom object with a custom name
# # https://docs.python.org/3.14/tutorial/classes.html


# Eighth Example

# def main():
#     student = get_student()
#     if student["name"] == "Padma": 
#         student["house"] = "Ravenclaw" # indexing into the student dictionary using the house key
#     print(f"{student['name']} from {student['house']}")
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house} # returning the dictionary - dict is mutable
# 
# if __name__ == "__main__":
#     main()
# 
# # adding back in the Padma if conditional

# Seventh Example

# def main():
#     student = get_student() 
#     print(f"{student['name']} from {student['house']}")
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house} # returning the dictionary
# 
# if __name__ == "__main__":
#     main()
# 
# # cleaning up the Sixth Example

# Sixth Example - introduce return list in get_students()

# def main():
#     student = get_student() 
#     print(f"{student['name']} from {student['house']}") # access the dict using the key
# 
# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student # returning a dictionary
# 
# if __name__ == "__main__":
#     main()
# 
# # reminder: be cautious of the double and single quote usage in f" string


# Sixth Example - introduce return list in get_students()

# def main():
#     student = get_student() 
#     if student[0] == "Padma": 
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}") # 
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house] # returning a list - this is mutable
# 
# if __name__ == "__main__":
#     main()

# Fifth Example

# def main():
#     student = get_student() # unpacking the return with two variables
#     if student[0] == "Padma": 
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}") # can access tuple values in the student variable
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # returning a tuple
# 
# if __name__ == "__main__":
#     main()
# 
# # this code throws TypeError: 'tuple' object does not support item assignment
# # because the tuple cannot take an assignment after returned
# # student[1] = "Ravenclaw" # not allowed for a tuple

# Forth Example - introduce tuple; tuples cannot change once they are created; this is immutable object

# def main():
#     student = get_student() # unpacking the return with two variables
#     print(f"{student[0]} from {student[1]}") # can access tuple values in the student variable
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # returning a tuple
# 
# if __name__ == "__main__":
#     main()
# 
# # when to use a tuple?
# # another way to increase the probability of code staying immutable


# Third Example - introduce tuple

# def main():
#     name, house = get_student() # unpacking the return with two variables
#     print(f"{name} from {house}")
# 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # returning one value called a tuple
# 
# if __name__ == "__main__":
#     main()


# Second Example

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
# 
# def get_name():
#     return input("Name: ")
# 
# def get_house():
#     return input("House: ")
# 
# if __name__ == "__main__":
#     main()


# First Example

# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")
# 
# # working code to introduce demo
