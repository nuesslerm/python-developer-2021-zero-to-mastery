# range(100) is a generator
# generators can use yield keyword, which can pause and resume the function

from time import time

range(100)
list(range(100))


def make_list(number):
    result = []
    for i in range(number):
        result.append(i * 2)
    return result


my_list = make_list(100)

# print(my_list)

# iterables that come from generators like range(), aren't saved in memory directly,
# but rather the generator yields one item at a time which is then consumed by e.g. the for loop
# that wants to use the iterable. range is therefore much more memory efficient than a regular list

# an iterable is any object in python with the dunder __iter__ method, so it's an object that can be looped through
# iterating is the act of taking an item from the iterable, doing something with it, and moving to the next one
# all generators are iterables but not all iterables are generators
# generators are functions


def generator_function(num):
    for i in range(num):
        # yield pauses the function when the generator is called by next() as arg,
        # it then waits for the next() function call with the generator as arg
        yield i


g = generator_function(50)

next(g)
next(g)
print(next(g))
print(next(g))
print(g)

# generators only keep the most recent value that was yielded in memory,
# so calling a generator with next() twice will only save the latest, second yield in memory
# it doesn't keep any other past or future values of the generator in memory

# if next() is called when the loop is already expired, ie. the last yielded result was generated with the
# last item in the iterable of the loop, then the next generator call with next() will throw a StopIteration exception

# when for loops are called with a generator like range(), then the StopIteration exception will cause
# the for loop to stop executing; this happens under the hood of the for-loop
# and allows for loops to work with generator iterables


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
    print("long_time")
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print("long_time2")
    for i in list(range(100000000)):
        i * 5


# long_time()
# long_time2()

# generators are faster than other iterables, e.g. lists


def gen_fun(num):
    for i in range(num):
        yield i


# under the hood of generators
# this is how a for loop works under the hood:
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(5, 10)
for i in gen:
    print(i)


# exercise: Fibonnaci Numbers
print("********************************")


class Fib:
    currentIdx = 0
    first = 0
    second = 1

    def __init__(self, idx):
        self.idx = idx

    def __iter__(self):
        return self

    def __next__(self):
        if Fib.currentIdx <= self.idx:
            Fib.currentIdx += 1
            temp = Fib.first
            Fib.first = Fib.second
            Fib.second = temp + Fib.second
            return temp
        raise StopIteration


def fib(index):
    fibfun = Fib(index)
    for num in fibfun:
        yield num


# fib_to_50 = fib(50)
# print(0, next(fib_to_50))
# print(1, next(fib_to_50))
# print(2, next(fib_to_50))
# print(3, next(fib_to_50))
# print(4, next(fib_to_50))
# print(5, next(fib_to_50))


def print_fib(index):
    fibfun = Fib(index)
    for num in fibfun:
        print("asdf", num)


print_fib(0)


def fib_list_create(index):
    fib_list = []
    fibfun = Fib(index)
    for num in fibfun:
        fib_list.append(num)
        print(num)
    return fib_list


# print(fib_list_create(200000))


def fib2(index):
    a = 0
    b = 1
    for _ in range(index + 1):
        yield a
        temp = a
        a = b
        b = temp + b


"""
fib_to_20 = fib2(20)
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
print(next(fib_to_20))
"""

for x in fib2(20):
    print("qwer", x)

"""
def fib2_list(index):
    a = 0
    b = 1
    result = []
    for _ in range(index + 1):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2_list(100))
"""