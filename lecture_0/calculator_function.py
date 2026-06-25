def main():
    x: int = int(input("What's x? "))
    print("x squared is", square(x)) # square function called here and passes argument of x

def square(n: int):
    return n * n # return sends the result to the caller of the function

main()

# this is a common pattern that the instructor introduced
# use of a main() function and call it at the bottom of the file