# conditional logic
is_old = 5
is_licenced = "None"

print(bool("hello"))
print(bool(5))
print(bool(""))
print(bool(0))
print(bool({}))
print(bool([]))
if is_old and is_licenced:
    print("you are old enough to drive. Happy driving!")
# elif not is_old:
#     print("you are not of age!")
else:
    print("you don't have a licence. Get away from the driver's seat!")

    print("okok")


# ternary operator == ternary expressions
# expressions evaluate to something

# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# short circuiting
is_friend = False
is_user = True

print(is_friend and is_user)

if not (is_friend and is_user):
    print("best friends")

# logical operators
print(4 > 5)
print(4 < 5)
print(4 == 5)
print(4 != 5)

print(1 < 2 > 3 < 5)

print(0 <= 0)
print(not (False))
print(not (0))
print(not ("adsf"))

# exercise: logical operators
is_magician = False
is_expert = False

# check if magician AND expert: "you are a master magician"
# check if magician but not expert: "at least you're getting there"
# if you're not a magician: "you need magic powers"

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
else:
    print("you need magic powers")

if is_magician:
    if is_expert:
        print("you are a master magician")
    else:
        print("at least you're getting there")
else:
    print("you need magic powers")

print(True == 1)  # True
print("1" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([1, 2] == [1])  # False

ware_house = {"something": 99}
new_ware_house = ware_house

print(ware_house["something"] is new_ware_house["something"])
print(ware_house["something"] == new_ware_house["something"])
print(ware_house is new_ware_house)
print(ware_house == new_ware_house)

# "is" keyword checks if variable is stored in same location in memory
print(1 is 1)  # True
print(True is True)  # True
print("1" is "1")  # True
print([] is 1)  # False
print(10 is 10.0)  # False
print([1, 2] is [1])  # False

# for loops
"""
for item in "Zero to Mastery":  # string is an iterable
    print(item)
    for item2 in [1, 2, 3]:  # list is an iterable
        print(item2, item)
        for item3 in {1, 3, 4, 5, 2, 3, 4, 5}:  # set is an iterable
            print(item3, item2, item)
            for item4 in (1, 3, 4, 5):  # tuple is an iterable
                print(item4, item3, item2, item)
                print("joooo")

print(item4)
"""

# iterable - string, list, dictionary, set, tuple
# iterate -> action of iterating over an iterable

user = {"name": "Golem", "age": 5006, "can_swim": False}

"""
for item in user:
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)
"""

for key, value in user.items():
    print(key, value)

# exercise: tricky total
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for item in my_list:
    total += item

print(total)

# range() function
# range returns a range object, special python object

for _ in range(100, -101, -5):
    print(_)

print(list(range(10)))

# enumerate() function

for i, char in enumerate(range(100)):
    if char == 50:
        print(f"index of {char} is: {i}")

# while loop
i = 0

while i < 50:
    print(i)
    i += 1
    break
else:  # used for cases where you only want another statement to execute if no break occurs in while loop
    print("done with all the work")

my_list = ["a", "2", "c"]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

"""
while True:
    response = input("say something:\n")
    if response == "bye":
        break
"""

# break, contiue, pass

for item in my_list:
    continue
    # print(item)

# pass doesn't do anything, it's just a placeholder to put in your code, so that loops don't break,
# when you don't have any executable code in the loop scope yet

# for item in my_list:
# comment without pass throws error

for item in my_list:
    # comment with pass doesn't throw error
    pass

# python GUI
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


"""
for row in picture:
    parsed_row = list(range(len(row)))
    for idx, item in enumerate(row):
        if item == 0:
            parsed_row[idx] = " "
        else:
            parsed_row[idx] = "-"
"""

"""
parsed_picture_string = ""

for row in picture:
    parsed_row_string = ""
    for item in row:
        if item == 0:
            parsed_row_string += " "
        else:
            parsed_row_string += "*"
    parsed_picture_string += f"{parsed_row_string}\n"

guified_picture = parsed_picture_string[:-2]

print(guified_picture)
"""

# code should be:
# clean
# readable
# predictable
# DRY

for row in picture:
    for pixel in row:
        if pixel:
            print("*", end="")
        else:
            print(" ", end="")
    print("", end="\n")


# exercise: check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n", "n"]

duplicates = []

for value in some_list:
    if value in duplicates:
        continue

    count = some_list.count(value)
    if some_list.count(value) > 1:
        duplicates.append(value)
        print(f"{value} is duplicate and exists {count} times")

# functions
def say_hello():
    print("hellooooo")


say_hello()


def show_tree():
    for row in picture:
        for pixel in row:
            if pixel:
                print("*", end="")
            else:
                print(" ", end="")
        print("", end="\n")


# note: there's no hoisting in python. make sure to define functions BEFORE calling the function
show_tree()
show_tree()
show_tree()

# parameters are input variables of a function
# a function is defined with parameters
# arguments are the actual values that are assigned to the parameters when calling a function
# a function is called/invoked with arguments


def say_hello2(name, emoji):
    print(f"hello {name} {emoji}")


# positional arguments, are arguments that just contain the value that the parameter should assume
# when the function is called, the assignment to parameters takes place in the exact order that the
# parameters of the function are listed
say_hello2("markus", "👋")

# keyword arguments, are arguments that mention the parameter name when calling the function, eg.
say_hello2(emoji="🚀", name="kavi")

# default parameters
def say_hello3(name="Joooo", emoji="💻"):
    print(f"hello {name} {emoji}")


say_hello3()

# function return


def sum_values(num1, num2):
    return num1 + num2


print(sum_values(4, 5))

# a function should do one thing really well
# a function should return something

total = sum_values(14, 2)
print(sum_values(10, total))


def sum_values2(num1, num2):
    def sum_values3(num3, num4):
        return num1 + num2

    return sum_values3(num1, num2)


total = sum_values2(14, 2)
print(sum_values2(10, total))

# methods vs functions

# list()
# print()
# max()
# min()
# input()


def some_random_stuff():
    pass


some_random_stuff()

print("hellllooooo".capitalize())

# docstrings
def test(a):
    """
    This is a docstring\n
    Info: this function tests and prints param a
    """
    print(a)


test("1232222")

# help(test)

print(test.__doc__)

# clean code
def is_even(num):
    return num % 2 == 0


print(is_even(50))

# *args
# **kwargs -> keyword args


def super_func(*args, **kwargs):
    # args are set as a tuple, ie. iterable
    print(args)
    print(kwargs)
    total = 0
    for value in kwargs.values():
        total += value

    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# rule: params, *args, default parameters, **kwargs


def super_func2(name, *args, i="hi", **kwargs):
    print(name)
    print(i)
    print(args)
    print(kwargs)
    total = 0
    for value in kwargs.values():
        total += value

    return sum(args) + total


# you can reassign the default param by using the keyword argument method of calling arguments
# when also using *args as part of the function
print(super_func2("markus", 1, 2, 3, 4, 5, i="jooo", num1=5, num2=10))


def highest_even(li):
    max = None
    for num in li:
        if num % 2 == 0 and (max == None or num > max):
            max = num
    return max


def highest_even2(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return max(evens) if len(evens) else None


print(highest_even([11, 10, 2, 3, 4, 5, 156, 6, 7, 8, 9]))
print(highest_even([11, 9, 7]))
print(highest_even2([11, 10, 2, 3, 4, 5, 156, 6, 7, 8, 9]))
print(highest_even2([11, 9, 7]))

# walrus operator
a = "helllllloooooo"

# if (n := len(a)) > 10:
#     print(f"too long {n} elements")

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)

# scope - what variables do I have access to?
total = 100  # global scope


def some_func():
    another_total = 100  # function scope
    print(another_total)


# print(another_total)  # doesn't work because you can't access function scope from global scope

# scope exercise
a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())

# 1 - start checkinf if variable is in local scope
# 2 - if varibale not in local scope, is there a parent local scope?
# 3 - if no parent local scope, is the variable defined in global scope?
# check if "variable" is part of the built in python functions
# parameters are part of local function scope


def count2():
    total = 0

    def count_up():
        nonlocal total
        total += 1
        return total

    return count_up()


count2()
count2()
print(count2())

# generators
def create_generator():
    i = 0
    while True:
        i += 1
        yield i


generator = create_generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# global keyword

total = 0


def count3(total):
    total += 1
    return total


print("count", count3(count3(count3(total))))


def count4():
    global total
    total += 1
    return total


count4()
count4()
count4()
count4()

print("count", count4())

# nonlocal keyword
def outer():
    x = "local"

    def inner():
        # if commented outer() prints inner: nonlocal, outer: local
        # if left untouched outer() prints inner: nonlocal, outer: nonlocal,
        # because x of the inner scope is technically a new variable and
        # different to the other x defined in the outer scope.
        # by using nonlocal x we say that inner x is supposed to be the same varibale
        # as in the outer scope, so it modifies the outer scope
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()

# why do we have scope?
# among other things it allows us to preserve memory by only defining funcion scope variables in memory
# when a function is called, after function execution the python garbage collector can clear up the
# memory usage by destroying the function scope variables