# Fourth Example - introduce randint function

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)


# Third Example - introduce randint function

# import random
# 
# number = random.randint(1, 10)
# print(number)


# Second Example - introduce from keyword

# from random import choice
# 
# coin = choice(["heads", "tails"]) # now choice can be called directly
# print(coin)


# First Example - introduce import and random library

# import random
# 
# coin = random.choice(["heads", "tails"])
# print(coin)
# 
# 
# # import brings functionality into a program
# # https://docs.python.org/3.14/library/random.html
