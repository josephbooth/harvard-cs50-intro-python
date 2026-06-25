# Sixth Example

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size) # a way to decompose the inner loop

def print_row(width):
    print("#" * width)

main()

# Fifth Example

# def main():
#     print_square(3)
# 
# def print_square(size):
#     for i in range(size):
#         print("#" * size) # a pythonic way to accomplish the inner loop j function
# 
# main()

# Fifth Example

# def main():
#     print_square(3)
# 
# def print_square(size):
#     
#     # For each row in square
#     for i in range(size):
# 
#         # For each brick in row
#         for j in range(size):
# 
#             # Print brick
#             print("#", end="")
#         
#         print() # this adds a newline to the output
# 
# main()

# outputs a 3 x 3 of hash marks in the terminal

# Forth Example

# def main():
#     print_row(4)
# 
# def print_row(width):
#     print("?" * width) # pythonic way to do this
# 
# main()

# Forth Example

# def main():
#     print_column(3)
# 
# def print_column(height):
#     print("#\n" * height, end="") # an acceptable pythonic way to do this
# 
# main()

# Third Example

# def main():
#     print_column(3)
# 
# def print_column(height):
#     for _ in range(height):
#         print("#")
# 
# main()

# Second Example

# for _ in range(3):
#     print("#")

# First Example

# print("#")
# print("#")
# print("#")

