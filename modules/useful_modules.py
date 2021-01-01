from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7]

# Counter creates a dictionary from iterable with key-value pairs as item: count
print(Counter(li))

sentence = "d oiafsjodi jasofi jaosdj foaisdjofia jsdoifj asoid"
print(Counter(sentence))

# defaultdict's first arg is a callback that returns the default in case the key isn't present in dict
dictionary = defaultdict(lambda: "doesn't exist", {"a": 1, "b": 2, "c": 3})
print(dictionary["a"])
print(dictionary["d"])

# d2 = OrderedDict()
d2 = {}
d2["a"] = 1
d2["b"] = 2
print(d2)

# d3 = OrderedDict()
d3 = {}
d3["b"] = 2
d3["a"] = 1
print(d3)

"""
Recently, the Python has made Dictionaries ordered by default! 
So unless you need to maintain older version of Python (older than 3.7), 
you no longer need to use ordered dict, you can just use regular dictionaries!
"""
d4 = {"d": 2, "c": 100}
d5 = {"c": 100, "d": 2}

# even though dicts are now ordered the result of this will still be True because
# the standard dictionaries don't take order into account when being compared to one another
# as long as all key-value pairs are the same (in any order) the result will be True
print(d2 == d3)
print(d4 == d5)
