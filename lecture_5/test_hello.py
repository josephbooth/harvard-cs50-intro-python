# Fourth Example - how a loop can be used to test different values

from hello import hello

def test_defaul():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

# be careful with the complexity of tests
# avoid a situation where a test for a test is needed - do not do this


# Third Example - create different functions for different test cases

# from hello import hello
# 
# def test_defaul():
#     assert hello() == "hello, world"
# 
# def test_argument():
#     assert hello("David") == "hello, David"
# 
# # break out the tests for better coverage when running
# # pytest test_hello.py from the command line
# # this can help isolate what might be causing an error in code
# # by having multiple test functions

# Second Example

# from hello import hello
# 
# def test_hello():
#     assert hello("David") == "hello, David"
#     assert hello() == "hello, world"


# First Example

# from hello import hello
# 
# def test_hello():
#     hello("David") == "hello, David"
# 
# # this doesn't work initally because the first example in hello.py
# # does not return a value from the function