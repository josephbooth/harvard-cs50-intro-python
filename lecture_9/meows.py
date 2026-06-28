# Thirteenth Example

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int) # added default and type
args = parser.parse_args() # this handles the order parsing for the programmer

for _ in range(int(args.n)):
    print("meow")

# default now handles when user does not submit a -n N
# type=int does the conversion of the N value when entered by user


# Twelfth Example - argparse library supports the passing in of options via command line

# import argparse
# 
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args() # this handles the order parsing for the programmer
# 
# for _ in range(int(args.n)):
#     print("meow")
# 
# 
# # https://docs.python.org/3.14/library/argparse.html
# # argparser has access to sys.argv
# # there is a convention to have a -h or --help for command line programs
# # % python3 meows.py -h
# # usage: meows.py [-h] [-n N]
# # 
# # Meow like a cat
# # 
# # options:
# #   -h, --help  show this help message and exit
# #   -n N        number of times to meow
 

# Eleventh Example - how to handle switches or flags

# import sys
# 
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")
# 
# # python meows.py -n 3
# # command line arguments are those that appear after the file name

# Tenth Example

# import sys
# 
# if len(sys.argv) == 1:
#     print("meow")
# else:
#     print("usage: meows.py")
# 
# # reminder sys.argv are the arguments being passed into the program
# # from the command line


# Ninth Example

# def meow(n: int) -> str:
#     """
#     Meow n times.
#     
#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :retype: str
#     """
#     return "meow\n" * n
# 
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")
# 
# # tools can be used to extract the docstrings
# # conventions for this documentation style
# # the syntax of the comment is called restructured text
# # it's not enforced by the language
# # tools use this convention to document functions
# # does not have anything to do with type hints
# # this is a third party convention so tools can generate docs, web page, etc.


# Eighth Example - introduce docstrings

# def meow(n: int) -> str:
#     """ Meow n times. """ # this is a docstring
#     return "meow\n" * n
# 
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")
# 
# # docstrings can be used by tools to produce documentation
# # https://peps.python.org/pep-0257/


# Seventh Example

# def meow(n: int) -> str:
#     return "meow\n" * n
# 
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")
# 
# # % python3 meows.py
# # Number: 3
# # meow
# # meow
# # meow


# Sixth Example

# def meow(n: int) -> None: # the -> None is a return hint added so mypy can help find errors
#     for _ in range(n):
#         print("meow")
# 
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)
# 
# # mypy meows.py shows the return type error

# Fifth Example

# def meow(n: int):
#     for _ in range(n):
#         print("meow")
# 
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)
# 
# # this code has an error
# # % python3 meows.py
# # Number: 3
# # meow
# # meow
# # meow
# # None

# Fourth Example

# def meow(n: int): # this is a type hint : int
#     for _ in range(n):
#         print("meow")
# 
# number: int = int(input("Number: ")) # added the int function to change type
# meow(number)
# 
# # mypy meows.py shows this code now passes


# Third Example - introduce type hints

# def meow(n: int): # this is a type hint : int
#     for _ in range(n):
#         print("meow")
# 
# number: int = input("Number: ") # : int is the type hint on the variable
# meow(number)
# 
# # type hints are not enforced by the language
# # show how mypy works
# # this is a tool for the programmer to run to find an issue
# # mypy meows.py to see errors

# Third Example - code example to setup the issue of type error

# def meow(n):
#     for _ in range(n):
#         print("meow")
# 
# number = input("Number: ")
# meow(number)
# 
# # this code throws a type error
# 
# # had to install mypy for this demo
#
# # https://mypy.readthedocs.io/en/stable/
# 
# # % python3 -m pip install --break-system-packages mypy    
# # Collecting mypy
# #   Downloading mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.3 kB)
# # Collecting typing_extensions>=4.6.0 (from mypy)
# #   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
# # Collecting mypy_extensions>=1.0.0 (from mypy)
# #   Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
# # Collecting pathspec>=1.0.0 (from mypy)
# #   Downloading pathspec-1.1.1-py3-none-any.whl.metadata (14 kB)
# # Collecting librt>=0.11.0 (from mypy)
# #   Downloading librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (1.3 kB)
# # Collecting ast-serialize<1.0.0,>=0.3.0 (from mypy)
# #   Downloading ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (1.3 kB)
# # Downloading mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl (13.7 MB)
# #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.7/13.7 MB 40.3 MB/s  0:00:00
# # Downloading ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl (1.2 MB)
# #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 27.9 MB/s  0:00:00
# # Downloading librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl (143 kB)
# # Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
# # Downloading pathspec-1.1.1-py3-none-any.whl (57 kB)
# # Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
# # Installing collected packages: typing_extensions, pathspec, mypy_extensions, librt, ast-serialize, mypy
# # Successfully installed ast-serialize-0.5.0 librt-0.11.0 mypy-2.1.0 mypy_extensions-1.1.0 pathspec-1.1.1 typing_extensions-4.15.0


# Second Example - introduce class constant

# class Cat:
#     MEOWS = 3 # only available to the class
# 
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")
# 
# cat = Cat()
# cat.meow()

# First Example - introduce constant variable

# MEOWS = 3
# 
# for _ in range(MEOWS):
#     print("meow")
# 
# # use of all caps is convention not an enforced language rule