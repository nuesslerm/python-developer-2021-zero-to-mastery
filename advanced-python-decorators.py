# decorators have @ sign and some name
# @classmethod
# @staticmethod

# in python functions are first class objects
# this means that they can be passed as arguments to other functions


from functools import reduce
from time import time


def hello():
    print("helllooo")


greet = hello
del hello  # del keyword removes object reference from memory

print(greet)
greet()
# -> greet still works, even though hello was deleted, because it still points
# to the function body's location in memory, ie. it still has a reference
# to the print("helllooo") part of the hello() function which was deleted
# only the hello() function's reference to that function body was deleted, not the function body itself,
# because python is smart enough to understand that the function body is still used by greet
# if there wasn't such a function as greet that points to the same function body as
# the deleted hello function, then also the function body would be deleted,
# because it wouldn't be needed by other functions anymore


def new_func(func):
    func()


def say_hi():
    print("hi")


new_func(say_hi)

# decorators use this function currying under the hood
# decorators supercharge a function, ie. add extra functionality to a function

# higher order functions HOC
# greet2 is an HOC because it accepts another function as an argument
def greet2(func):
    func()


# greet3 is an HOC because it returns a function
def greet3():
    def func():
        return 5

    return func


# map, filter, reduce, zip are all HOCs

# decorators
# a function that wrapps another function to enhance or change it


# to use @ with my_decorator, the defined decorator HOC needs to follow this exact pattern
# of defining a wrapper function in its scope, then calling the function,
# and at the end returning the wrapper
# decorator pattern:
"""
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func
"""


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        # print(len(("1", "2", 3, 88)))
        # print(len(str(args[1])))
        num_stars = (
            reduce(lambda acc, curr: acc + len(str(curr)), args, len(args) - 1) * "*"
        )
        print(num_stars)
        func(*args, **kwargs)
        print(num_stars)

    return wrap_func


@my_decorator  # @ sign is just wrapping the say1 function in the my_decorator HOC
def say1(string2, emoji):
    print(string2, emoji)


# -> a = my_decorator(say1)
# a()
# -> my_decorator(say1)() # immediately invoke an HOC by adding ()
# at the end of the HOC after initialising the HOC with arguments
# only works if HOC returns another function like e.g. a decorator


say1("helloooo", 123)
say1("see ya later", 2324)

# why do we need decorators?
# practical applications
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


# long_time()

# exerise: @authenticated
# from functools import reduce
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {"name": "Sorna", "valid": True}
user2 = {"name": "Markus", "valid": True}
user3 = {"name": "Kavi", "valid": True}


def authenticated(fn):
    def wrapper(*args):
        # valid = reduce(lambda acc, curr: True if acc[0] and curr["valid"] else False, args, True)
        allInvalid = list(filter(lambda x: not x["valid"], args))

        if not len(allInvalid):
            fn(*args)
        else:
            listAllInvalid = list(map(lambda x: x["name"], allInvalid))
            print(f"not authenticated: {listAllInvalid}")

    return wrapper


@authenticated
def message_friends(*users):
    print("message has been sent")


message_friends(user1, user2, user3)

"""
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {"name": "Sorna", "valid": True}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
"""