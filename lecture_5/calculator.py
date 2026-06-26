# Second Example

def main():
    x = input("What's x? ") # removed the int function
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

# this is setup so that a user can input a str
# in test_calculator.py there is a test for this

# First Example

# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))
# 
# def square(n):
#     return n * n
# 
# if __name__ == "__main__":
#     main()
# 
# # the dunder methods protect from main() running
# # when importing into other files