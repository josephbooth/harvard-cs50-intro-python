# Third Example

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")



# Second Example - inherit

# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
# 
#     ...
# 
# # the super is (Wizard) in this demo        
# class Student(Wizard): # Student will inherit from Wizard
#     def __init__(self, name, house):
#         super().__init__(name) # programmatically accessing the Parent or the super class
#         self.house = house
# 
#     ...
# 
# # the super is (Wizard) in this demo
# class Professor(Wizard): # Professor will inherir from Wizard
#     def __init__(self, name, subject):
#         super().__init__(name) # programmatically accessing the Parent or the super class
#         self.subject = subject
#     
#     ...
# 
# wizard = Wizard("Albus")
# student = Student("Harry", "Gryffindor")
# professor = Professor("Severus", "Defense Against the Dark Arts")

# First Example - introduce inheritance

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.house = house
# 
#     ...
# 
# class Professor:
#     def __init__(self, name, subject):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.subject = subject
#     
#     ...
# 
# # setting up the demo