"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730356913"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")
a: int = (randint(1,100))
if a <= 25:  
    print("You will get a pet this year")
else:
    if a <= 50:
        print("You will find out a deep family secret tomorrow")
    else: 
        if a <= 75:
            print("Your mom wants you to call her")
        else: print("There will be a gift in your future")
print("Now, go spread positive vibes!")
