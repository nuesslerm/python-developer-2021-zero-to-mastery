import re

# r stands for raw string. raw strings are best for regex patterns
# to avoid python from adding any special functionality to the string, as it's not needed
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string2 = "b@b.com"

# print("search" in string2)

a = re.search(pattern, string2)
b = pattern.search(string2)
c = pattern.findall(string2)
d = pattern.fullmatch(string2)
e = pattern.match(string2)
print(b.span())
print(b.start())
print(b.end())
print(b.group())
print("c", c)
print(1, d)
# print(e.group())

# advanced patterns
