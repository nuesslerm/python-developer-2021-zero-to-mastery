# how to organise python code with modules and packages
# a module is a file containing reusable code in form of functions, classes, etc.
# a package is a folder that contains modules

# imports everything as normal functions, ie. multiply, divide, max, etc
# not recommended because imported function could override another existing function
# always be explicit and declare exactly what you want to import
from utility import *

# import utility # import module directly
# import shopping.more_shopping.shopping_cart # import module directly from package
from shopping.more_shopping import shopping_cart as whatsGood
import random as oulala
import sys
import pyjokes

# from random import shuffle as oulala

# print(utility)
# print(shopping.more_shopping.shopping_cart)

if __name__ == "__main__":
    print(multiply(2, 23))
    print(divide(23, 2))

    print(whatsGood.buy("apple"))

    print(max([1, 2, 3, 4, 5, 232, 23, 4, 4]))

    # __main__ is always given to the file that is the root of code execution
    print(__name__)
    if __name__ == "__main__":
        print("please run this print statement")

# python built-in modules
# they come with python, when downloading the python interpreter
# https://docs.python.org/3/py-modindex.html


# print(random)
# help(random)
# print(dir(random))

print(oulala.random())
print(oulala.randint(0, 10))
print(oulala.choice(["a", "b", "c", 4, 5, 6]))
print(oulala.shuffle(["a", "b", "c", 4, 5, 6]))

# my_list = ["a", "b", "c", 4, 5, 6, 7, 8, 9]
# oulala(my_list)
# print(my_list)

# print(sys)

# filename = sys.argv[0]
# first = sys.argv[1]
# last = sys.argv[2]

# print(f"hi {first} {last}")

# except for the built-in modules you can also download and install extenral 3rd party modules from the internet
# https://pypi.org/

# help(pyjokes)
# print(dir(pyjokes))
# print(pyjokes.get_joke("de", "twister"))
print(pyjokes.get_joke("en", "neutral"))
# print(pyjokes.get_joke("en", "all"))
# print(pyjokes.get_jokes("dee"))
