# file I/O
# file input / output

# input image
# out compressed image

"""
my_file = open("python-advanced/test.txt")

print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
# python uses a cursor to read the file,
# which needs to be reset with seek(0) at the end of a read operation
print(my_file.read())
my_file.seek(0)
print("********************************")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
# print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())  # returns list that contains the entire file line by line
my_file.seek(0)

my_file.close()

print(my_file.readline())  # doesn't work anymore because file was already closed
"""

# mode needs to be specified as "r" = read or "w" = write to allow read and/or write operations
# default mode is mode="r"
# mode="r+" means read and write, write will start with cursor at 0 and overwrite text from there, mode="r+" cannot create new files
# mode="a+" means append and read, cursor will automatically be set to the end of the file, so writing will append text
# mode="w" means write, write will assume it's a new file and clear the file's content before writing, mode="w" can create new files
"""
with open("./folder/hellloooo.txt", mode="w") as my_file:
    text = my_file.write(":)")
    print(text)
    my_file.seek(0)
    # print(my_file.readline())
"""

# filepaths
# depends on where the python script is executed and based on that location you can refer to files by their
# relative path to that execution location, or you can use the absolute filepath, which is denoted by
# something like /Users/nuesslerm/...
# you can try out the package pathlib

# file i/o errors
try:
    with open("./folder/test2.txt", mode="r+") as my_file:
        text = my_file.read()
        print(text)
except FileNotFoundError as err:
    print("file does not exist in designated location")
    raise err
except IOError as err:
    # can e.g. be raised by setting the open mode to something non-existent like mode="x"
    print("IO error")
    raise err