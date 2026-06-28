# Fifth Example - introduce list comprehension

def main():
    yell("This", "is", "CS50")

def yell(*words):
                  # give me the uppercase word for each word in words list
    uppercased = [word.upper() for word in words] # pythonic way to create a list comprehension
    print(*uppercased)

if __name__ == "__main__":
    main()

# this one will take some practice to wrap my head around
# list comprehension is a python feature


# Fourth Example - introduce map

# def main():
#     yell("This", "is", "CS50")
# 
# def yell(*words):
#     uppercased = map(str.upper, words) # str.upper is being passed as a function notice no () after upper
#     print(*uppercased)
# 
# if __name__ == "__main__":
#     main()


# Third Example

# def main():
#     yell("This", "is", "CS50")
# 
# def yell(*words): # this is a variable argument *args
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased) # used the * to unpack the list
# 
# if __name__ == "__main__":
#     main()

# Second Example

# def main():
#     yell(["This", "is", "CS50"])
# 
# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased) # used the * to unpack the list
# 
# if __name__ == "__main__":
#     main()


# First Example

# def main():
#     yell("This is CS50")
# 
# def yell(phrase):
#     print(phrase.upper())
# 
# if __name__ == "__main__":
#     main()
