"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730356913"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    
    print(fortune_cookie())



# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    a: int = (randint(1, 100))
    if a <= 25:  
        return ("You will get a pet this year")
    else:
        if a <= 50:
            return ("You will find out a deep family secret tomorrow")
        else: 
            if a <= 75:
                return ("Your mom wants you to call her")
            else: 
                return ("There will be a gift in your future")
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()