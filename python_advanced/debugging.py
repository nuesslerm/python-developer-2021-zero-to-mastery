# debugging

# use linting
# learn how to read errors
# pdb python debugger


import pdb


def add(num1, num2):
    # print(num1, num2)
    pdb.set_trace()
    return num1 + num2


print(add(4, 2))