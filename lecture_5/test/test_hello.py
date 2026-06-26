#First Example

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# demo is using this file as a demo for the __init__.py
# apparently using the __init__.py name tells python that 
# this is not just a file... but a package
# creating __init__.py in the test directory
# with the package setup... from the command line I can run pytest test
# where test is the directory within lecture_5
# pytest will go through and run all tests in the directory
# so adding additional test_ files in the test directory allows for a suite of tests
# to be conducted