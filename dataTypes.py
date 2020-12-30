# Data Types
# int
""" 
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(0)) 
"""

# float
""" 
print(type(2 / 4))
print(type(0.00001212))
print(type(9.9 + 1.1))

print(2 ** 3)
print(8 / 2)
print(9 // 2)
print(5 % 4) 
"""

# math functions
print("round", round(3.1))
print("abs", abs(-20))

# operator precedence
print("calculate", 20 - 3 * 4)

# data type: complex for complex numbers
# complex

# get binary representation of number
print(bin(5))
print(int("0b101", 2))

# variables
# snake_case
# start with lowercase or underscore -> if it starts with underscore it's marked as a private variable
# letters, numbers, underscores
# case sensitive
# don't overwrite keywords
# don't create variables that start with dunders (double underscores __asdf)

# constants
# variables in all caps

# iq = 100 expression
# user_age = (iq / 4 expression); entire line is a statement; a statement is a line of code that calculates/achieves something

# augmented assignment operator
some_value = 5
some_value = some_value + 2
some_value += 2
some_value -= 2
some_value *= 2

print(some_value)

# bool
True
False

name = "Markus"
is_cool = False
print(is_cool)

is_cool = True
print(is_cool)

# convert to boolean
print(bool(1))  # True
print(bool(0))  # False
print(bool("True"))  # True
print(bool("False"))  # True
print(bool("Asdf"))  # True

# str
print(type("hi hello there"))
username = "supercoder"
userpassword = "supersecret"
long_string = """WOW
asdf
fghj
yxcv
"""
print(long_string)

full_thing = username + " " + userpassword
print(full_thing)

# string concatenation
print("hello" + " markus")
# print("hello" + " markus" + 5) -> doesn't work because of int at the end

# type conversion
print(type(int(str(100))))

# escape sequence
weather = 'It\'s tabbed \t "escaped" \n \\ sunny jooooo'
print(weather)

# formatted strings / f-strings
name = "John"
age = 55
print("hi " + name + ". You are " + str(age) + " years old.")
# add f to the beginning of the string to make it a string literal / formatted string, new in python3
# we don't need the str() type conversion when using formatted strings
print(f"hi {name}. You are {age} years old.")
# formatted strings in python2
print("hi {}. You are {} years old.".format(name, age))
# switch usage around by specifying variable position
print("hi {1}. You are {0} years old.".format(name, age))
# override values to formatted strings
# print("hi {1}. You are {0} years old.".format(name="Markus", age=100))
# override values and specify varibales by name when using format strings
print("hi {age}. You are {name} years old.".format(name="Markus", age=100))

# string indices
selfish = "me me me"
#         "01234567"
print(selfish[0:8:1])
print(selfish[:])
print(selfish[::])
print(selfish[0:])
print(selfish[0::])
print(selfish[0::2])
print(selfish[0:-1])
print(selfish[0:8])
print(selfish[:-1])
print(selfish[::-1])
print(selfish[::-2])
# str[start:stop:stepover]

# string objects in python are immutable
# selfish[0] = "1" -> TypeError: 'str' object does not support item assignment
# you can't reassign part of a string
# you can only reassign the entire string (this'll delete the old string reference and create a whole new one)

# build-in functions / methods
greet = "helloooooo"
# len is a function
# methods are functions that exist on an object, e.g. str.format() is a method that exists on the str object
print(len("0123456"))
print(greet[: len(greet)])

quote = "to be or not to be"
print(quote.capitalize())
print(quote.upper())
print(quote.count("o"))
print(quote.replace("be", "have been"))
print(quote.replace("be", "have been").count("e"))

# exercise: type conversion
"""
birth_year = input("What year were you born?\n")
print(type(birth_year))
age = 2020 - int(birth_year)
boolAge = 2020 - bool(birth_year)
print(f"You're {age} years old")
print(f"You're {boolAge} years old")
"""

# single line comment
""" 
multi-
line-
comment
"""
# add comments only when necessary, code should be self-documenting

# exercise: password checker
"""
username = input("Enter username:\n")
password = input("Enter password:\n")

password_length = len(password)

print(
    f"Hi {username}.\nYou're password {password_length * '*'} is {password_length} chars long"
)
"""

# lists in python are similar to arrays in JS
# list is a data-structure
li = [1, 2, 3, 4, 5, 6]
li2 = [1, "234", "hi", True, 5, 6]

amazon_cart = ["some", "some_else", 123, "cool toys", "nahhhh"]

print(amazon_cart[0])
print(amazon_cart[1])

# list slicing
print(amazon_cart[0:3])
print(amazon_cart[0:2:])
print(amazon_cart[0::2])

# lists are mutable
amazon_cart[0] = "laptop"
print(amazon_cart)
print(amazon_cart[1:3])
print(amazon_cart[0:3])

# new variable is just assigned the reference to amazon_cart
new_cart = amazon_cart
# to copy a list you need to use list slicing to create a true copy
new_cart = amazon_cart[:]

new_cart[0] = "what"
print(amazon_cart)
print(new_cart)

# maticies are special types of multi-dimensional lists/arrays
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]
print(matrix)
print(matrix[0][0])

# list methods
basket = [1, 2, 3, 4, 5]

# append changes list in place, it doesn't create a new list
new_list = basket.append(100)
print(basket)
print(new_list)

# insert changes list in place
# inserts new element before specified index
basket.insert(2, 100)
print(basket)

# list extend changes list in place
basket.extend([1232, 1232])
print(basket)

# pop changes list in place and returns popped element
basket.pop(0)
print(basket)
# remove will remove the fist instance of the element found in the list
basket.remove(1232)
basket.remove(100)
basket.remove(100)
basket.remove(4)
print(basket)

# clear changes list in place
basket.clear()
print(basket)

basket2 = ["a", "b", "c", "d", "e", "d", "x"]
# index
# print(basket2.index("d", 0, 3)) -> error
print(basket2.index("d", 0, 4))
print("d" in basket2)

# count
print(basket2.count("d"))

# sort changes list in place
"""
basket2.sort()
print(basket2)
"""

# sorted sorts and creates a new list
print(sorted(basket2))
print(basket2)

# copy will copy the list and return a new list
new_basket = basket2.copy()
print(new_basket)

# reverse changes the list in place
basket2.reverse()
print(basket2)

# common list patterns
print(basket2[::-1])
print(basket2)

# range will return a range of numbers that are indexed into a list if used in combination with the list initialiser
print(list(range(1, 100)))
print(list(range(100)))  # starts from 0

# join is a method on str object -> used for creating a string from a list of items
sentence = " "
new_sentence = sentence.join(["hi", "my", "name", "is", "markus"])
new_sentence2 = " ".join(["hi", "my", "name", "is", "markus"])
print(new_sentence2)

# list unpacking -> similar to array destructuring in JS
a, b, c, d, *other, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(e)


# dict for Dictionaries
# dict is a data structure, dict is a map of unordered key-value pairs
# unordered collections of key-value pairs (don't need to be unique)
# like a map in JS
dictionary = {
    b: 2,
    a: 1,
    c: 3,
}

dictionary2 = {
    "b": 2,
    "a": [
        1,
        2,
        3,
    ],
    "c": 3,
}

new_list = [dictionary, dictionary2]

print(dictionary[b])
print(dictionary)
print(dictionary2["b"])
print(dictionary2)

print(new_list[1]["a"][0])

"""
when to use lists and when to use dicts
* list have order, dicts don't have order (they're unsorted)
* dicts allow for more structured information storage with keys
"""

# dictionary keys can be anything that is immutable
# dictionary keys *should* to be unique, otherwise the latter entry will
# override the previous one when trying to query for dict entry

dictionary3 = {
    12: 2,
    d: "skdfjl",
    "a": [
        1,
        2,
        3,
    ],
    True: 3,
}
print(dictionary3)

# print(dictionary3["age"])
print(dictionary3.get("age"))
# get age from dictionary3, but if age doesn't exist return default value
print(dictionary3.get("age", 55))

user = dict()
print(user)

user3 = {"what": 123}
print(user3)

user2 = dict(name="Markus", age=55)
print(user2)

# check if item is in dictionary
"""
print("Markus" in user2)  # False because it only checks dict's keys
print(user2.keys())
print("Markus" in user2.keys())  # False because it only checks dict's keys
print(user2.values())
print("Markus" in user2.values())  # True because it checks dict's values
print(user2.items())
print(
    ("name", "Markus") in user2.items()
)  # True, because it checks for complete key, value pairs (ie. 2-tuples) in comma-separated form
"""

user3.clear()
print(user3)

user4 = user2.copy()
print(123, user4)
print(user4.pop("name"))

print(user2, user4)

# dict.popitem pops of last item
# remeber if the dict is hugely long then the order in the dict can be random so popitem doesn't
# necessarily return the last item that you inserted when working with very long lists

print(user2.popitem())
print(user2)

# update, updates a specific key-value pair or inserts it if it doesn't exist'
user2.update({"whatThe": "cool", "name": "Kavi"})
print(user2)

# classes -> custom types


# Specialised Data Types


# None is a special data type. similar to null in JS
a = None

print(a)

# tuple, like lists but immutable
# tuples are more performant than lists because they can't be changed / are immutable

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(4 in my_tuple)
print(6 in my_tuple)

print(user2.items())  # returns a list of 2-tuples

my_tuple = (1, 2, 3, 4, 5, 2)
new_tuple = my_tuple[1:2]

print(new_tuple)  # a tuple with only one item ends with a comma, e.g. (2,)

# tuple unpacking
x, y, *other = my_tuple
print(x, y, other)

print(len(my_tuple))
print(my_tuple.count(2))
print(my_tuple.index(2))

# set is a data structure
# like lists but all items need to be unique
# unordered collections of unique objects (ie. items in set don't have indices), will be returned in sorted format

my_set = {
    1,
    3,
    "asdf",
    5,
    "123",
    5,
    4,
    2,
}
print(my_set)

# remove all duplicates from a list
my_list = [1, 2, 3, 4, 4, 4, 4, 5]
print(set(my_list))

my_set2 = {1, 2, 3, 4, 4, 4, 5}
new_set = my_set2.copy()
new_set.clear()

print(1 in my_set2)
print(len(my_set2))
print(list(my_set2)[0])

print(my_set2)
print(new_set)

my_set = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3}
my_set3 = {4, 5, 6}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))  # doesn't update set, just reurns the difference
# print(my_set.discard(5)) # modifies set in place
# print(my_set.difference_update(your_set)) # modifies set in place, and removes items that are different
print(1, my_set.intersection(your_set))  # doesn't update set, returns the intersection
print(1, my_set & your_set)  # shorthand for intersection
print(my_set.isdisjoint(your_set))  # False because sets have some items in common
print(my_set2.isdisjoint(your_set))  # True because sets don't have any items in common
print(
    my_set.issubset(your_set)
)  # False because not all itmes of my_set are found in your_set
print(
    my_set3.issubset(your_set)
)  # True because all items of my_set3 are found in your_set
print(
    2, my_set.union(your_set)
)  # joins sets together and removes any duplicates, returns a new set
# my_set.union(your_set) === my_set | your_set # short-hand for union
print(2, my_set | your_set)
print(
    your_set.issuperset(my_set)
)  # False because your_set contains items that aren't found in my_set
print(
    your_set.issuperset(my_set3)
)  # True because your_set contains all items that are found in my_set3
print(my_set)