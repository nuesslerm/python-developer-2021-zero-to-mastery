# what is functional programming?
# separation of data and functions
# emphasis on simplicity where data and functions are concerned
# functions operate on well-defined data structures rather than assigning the data structure to an object
# general goals:
# clear + understandable
# easy to extend
# easy to maintain
# memory efficient
# DRY

# pure functions
# given the same input it will always return the same output
# a function should not produce any side effects
# a side effect is something that affects the outside world (outside of the function's local scope)
# pure functions mean less buggy code

wizard = {"name": "Merlin", "power": 50}


def attack(character):
    # if not character["power"]:
    #     character["name"] = 0
    return "you attacked with power of {power}".format(power=character["power"])


def multiply_by2(li):  # pure function
    new_list = []
    for item in li:
        new_list.append(item * 2)
    # if you use print in this function it would be considereda side-effect
    return new_list


print(multiply_by2([1, 2, 3]))

new_list2 = []

# unpure function because it has a side-effect in that it affects new_list2
# which is outside of the function's local scope
def another_multiply_by2(li):
    for item in li:
        new_list2.append(item * 2)
    return new_list2


my_list = [1, 2, 3]

# map, filter, zip, reduce
# map
def multiply_by3(item):
    return item * 3


# map creates a map object that can be converted to a list
print(list(map(multiply_by3, my_list)))


# filter
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)


# zip
your_list = [10, 20, 30]
your_list2 = [10, 20, 50, 40]

print(list(zip(your_list2, my_list, your_list)))
print(list(zip(my_list, your_list2)))

# reduce
from functools import reduce

my_list2 = [1, 2, 3, 4]


def accumulate_func(acc, curr):
    return acc + curr


print(reduce(accumulate_func, my_list2, 0))

# lambda expressions
# are functions that are only used once and then discarded
# are anonymous functions, so they don't need to be named

# lambda param: action(param)
# in one-liners action(param) immediately returns

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, curr: acc + curr, my_list))

print(my_list)

# exercise: lambda expressions

my_list = [5, 4, 3]

print(list(map(lambda num: num ** 2, my_list)))

# list sorting based on the second element in the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(sorted(a, key=lambda x: x[1]))

# sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)],key=lambda x: x[1], reverse=True)

# python feature: (list-/set-/dict-) comprehension
# comprehension is a shorthand for quickly creating iterables

my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# pattern: my_list = [param for param in iterable]
my_list3 = [char + "m" for char in "hello"]
my_list4 = [num * 2 for num in range(0, 100)]
my_list5 = map(lambda x: x % 2 == 0, [num ** 2 for num in range(0, 100)])
my_list6 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list3, my_list4)
print(my_list6)

# set and dict comprehensions
# set
my_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_set)

# dict
simple_dict = {"a": 1, "b": 2}
key_list = ["a", "b"]
value_list = [1, 2]

my_dict = {key: value ** 2 for key, value in simple_dict.items()}
# don't try to be overly clever
my_dict2 = {
    key + "m": value ** 3 for key, value in zip(key_list, value_list) if value % 2 == 0
}
my_dict3 = {num: num * 2 for num in [1, 2, 3]}

print(simple_dict.items())
print(my_dict)
print(my_dict2)
print(my_dict3)

# exercise: list comprehension
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)