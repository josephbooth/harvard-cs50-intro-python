# Fourth Example
import random

class Hat:
    
    houses = ["Grffyindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable

    @classmethod
    def sort(cls, name): # cls is short for class
        print(name, "in in", random.choice(cls.houses)) # no longer self

Hat.sort("Harry")

# Third Example - introduce @classmethod
# import random
# 
# class Hat:
#     
#     houses = ["Grffyindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable
# 
#     @classmethod
#     def sort(cls, name): # cls is short for class
#         print(name, "in in", random.choice(cls.houses)) # no longer self
# 
# Hat.sort("Harry")
# 
# # no longer need to instantiate a Hat object
# # @classmethod now allows for calling the method directly


# Second Example
# import random
# 
# class Hat:
#     def __init__(self):
#         self.houses = ["Grffyindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# 
#     def sort(self, name): # self always has to be added to the function
#         print(name, "in in", random.choice(self.houses))
# 
# hat = Hat() # instantiate an object of Hat assign to variable hat
# hat.sort("Harry")


# First Example

# class Hat:
#     def sort(self, name): # self always has to be added to the function
#         print(name, "in in", "some house")
# 
# hat = Hat() # instantiate an object of Hat assign to variable hat
# hat.sort("Harry")

