# Second Example - fix the hello function to have a return value - allows for testing

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()

# this is more testable because it allows testing of
# return values and arguments... not side effects
# recall side effects are things like the print statement output to console

# First Example

# def main():
#     name = input("What's your name? ")
#     hello(name)
# 
# def hello(to="world"):
#     print("hello, ", to)
# 
# if __name__ == "__main__":
#     main()

