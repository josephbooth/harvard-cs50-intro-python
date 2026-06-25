def main():
    # ask the user for their name
    name: str = input("What's our name? ")
    hello(name) # call function hello and pass the value of name to it

def hello(to="world"):
    print("hello,", to)

main() 

# the default value for the argument to a function can be set 

# functions must be declared in code prior to calling it
# meaning the function must exist to the computer prior to using it

# using a main function allows for functions to be declared further down the 
# file so that the developer doesn't constantly have to push code down the page to make room
# for functions to be declared before use. 

# sounds like a best practice is to always have a main function