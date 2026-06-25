# Ask the user for values of x and y
x: float = float(input("What's x? "))
y: float = float(input("What's y? "))

# Round the result of x + y for the user
# z: float = round(x + y)
# z: float = round(x / y, 2) 
z: float = x / y

print(f"{z:.2f}")
# print(f"{z:,}")

# int is a type and a function in python
# using : int is a type hint these are useful for humans and for some functions in VS Code
# x: int = int(input("What's x? "))
# y: int = int(input("What's y? "))

# https://docs.python.org/3/library/functions.html#round
# round(number, ndigits=None)
# ndigits is an optional "Named Parameter"

# print(f"{z:,}") the colon and comma format the output with commas between ever three digits
# example: 1,000 or 349,889,010

# print(f"{z:.2f}") the colon decimal point two f controls the number of decimals after the decimal point