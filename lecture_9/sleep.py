# Third Example - introduce generators and keyword yield

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i # yield keyword here returns small parts of the function at a time
    # yield returns what is called an iterator

if __name__ == "__main__":
     main()

# fix the large number error
# this allows 
# https://docs.python.org/3.14/howto/functional.html#generators
# https://docs.python.org/3.14/reference/simple_stmts.html#yield
# reminder ctrl + c will interrupt the console output




# Second Example

# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)
# 
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock
# 
# if __name__ == "__main__":
#      main()
#
# # this has an error when n becomes very large
# # entering in 1000000 basically breaks the program



# First Example

# n = int(input("What's n? "))
# 
# for i in range(n):
#     print("🐑" * i)