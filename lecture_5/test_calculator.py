# Sixth Example - introduce the pytest.raises function and with keyword

import pytest
from calculator import square 

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# testing to ensure the TypeError is raised properly
def test_str():
    with pytest.raises(TypeError):
        square("cat")
    
# adding a test for the str error
# added the pytest library itself to get to the raises method


# Fifth Example - create smaller test functions

# from calculator import square 
# 
# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9
# 
# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9
# 
# def test_zero():
#     assert square(0) == 0
# 
# # this is a strategy to test more completely for each program run
# # helps get through more tests

# Fourth Example - introduce pytest library and the concept of unit tests

# from calculator import square 
# 
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
# 
# # % pytest test_calculator.py 
# # notice that python3 is not used to call pytest
# 
# # to fix error calculator.py square function changed to multiplication
# 
# # https://docs.pytest.org/en/7.1.x/contents.html
# # required:
# # % python3 -m pip install --break-system-packages pytest
# # Collecting pytest
# #   Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
# # Collecting iniconfig>=1.0.1 (from pytest)
# #   Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
# # Collecting packaging>=22 (from pytest)
# #   Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
# # Collecting pluggy<2,>=1.5 (from pytest)
# #   Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
# # Collecting pygments>=2.7.2 (from pytest)
# #   Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
# # Downloading pytest-9.1.1-py3-none-any.whl (386 kB)
# # Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
# # Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
# # Downloading packaging-26.2-py3-none-any.whl (100 kB)
# # Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
# #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 33.2 MB/s  0:00:00
# # Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest
# # Successfully installed iniconfig-2.3.0 packaging-26.2 pluggy-1.6.0 pygments-2.20.0 pytest-9.1.1


# Third Example - use assert within a try: except: block

# from calculator import square 
# 
# # from allows the importation of a single function
# def main():
#     test_square()
# 
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:    
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:    
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:    
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:    
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")
# 
# if __name__ == "__main__":
#     main()
# 
# # demonstrating how this pattern starts to get unwieldly as test cases rise    

# Third Example - use assert within a try: except: block

# from calculator import square 
# 
# # from allows the importation of a single function
# def main():
#     test_square()
# 
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:    
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
# 
# if __name__ == "__main__":
#     main()

# Second Example - introduce assert

# from calculator import square 
# 
# # from allows the importation of a single function
# def main():
#     test_square()
# 
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
# 
# if __name__ == "__main__":
#     main()

# First Example

# from calculator import square 
# 
# # from allows the importation of a single function
# def main():
#     test_square()
# 
# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")
# 
# if __name__ == "__main__":
#     main()

# to throw errors during this demo...
# calculator.py square function is set to plus instead of multiply