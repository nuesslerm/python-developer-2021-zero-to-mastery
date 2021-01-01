# how to organise python code with modules and packages
# a module is a file containing reusable code in form of functions, classes, etc.
# a package is a folder that contains modules
import utility

import shopping.shopping_cart

print(utility)
print(shopping.shopping_cart)

print(utility.multiply(2, 23))
print(utility.divide(23, 2))


print(shopping.shopping_cart.buy("apple"))
