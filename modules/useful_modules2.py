import datetime
from array import array

# print(datetime.time(5, 45, 2))
print(datetime.date.today())

# array os more memory optimised

# arr = array("i", [1, 2, 3, "a"]) # doesn't work because all array elements are supposed to be signed integers, ie. "i"
arr = array("i", [1, 2, 3])


print(arr)
print(arr[0])