# OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type("hi"))
print(type([]))
print(type(()))
print(type({}))

# OOP is a paradigm


class BigObject:
    pass


obj1 = BigObject()
print(type(obj1))

# a class is a blueprint for an object
# instantiate class to create instances

# can I have private variables? -> NO, use _ underscore to denote private variables as a convention
class PlayerCharacter:
    # class object attribute, static attribute on class
    membership = True
    # __init__ is called a dunder method
    # you can assign default attribute values to __init__ attributes
    def __init__(self, name="anonymous", age=0):
        # if PlayerCharacter.membership: <- this is identical to below because it's a class attribute
        if self.membership and age > 18:
            # attributes
            self._name = name
            self._age = age

    def run(self):
        print("run")

    def shout(self, statement):
        """
        insert a statement to be shouted in all caps after character proclaims their name
        """
        print(f"my name is {self._name} and {statement.upper()}!!!!!")

    def return_self(self):
        return self

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Ted", num1 + num2)

    # staticmethod is similar to the classmethod above but you don't have access to the cls keyword, so you can't instantiate a new object
    @staticmethod
    def multiplying_thing(num1, num2):
        return num1 * num2


player1 = PlayerCharacter("Markus", 26)
# player2 = PlayerCharacter("Karl", 13) # because object attributes are only instantiated when age > 18, this player object instantiation will error out
player2 = PlayerCharacter("Kavi", 22)
player2.attack = 50

# print(player1)
# print(player2)
print(player1._name)
print(player2._name)
print(player1.membership)
print(player2.membership)
print(player2.attack)
player1.run()
player2.shout("pusheen is cute")

# help(player1)  # use help to get documentation in terminal

player3 = PlayerCharacter()

# player3.shout("what") # will error out because player3 was instantiated without an age so it defaulted to age=0

# @classmethod and @staticmethod

# print(player1.adding_things(1, 21232))
player4 = PlayerCharacter.adding_things(1, 21232)
player4.shout("what")
print(player4._age)

print(PlayerCharacter.multiplying_thing(2324, 2))

# overall class structure in python
class NameOfClass:
    class_attribute = "value"

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # code
        pass

        @classmethod
        def cls_method(cls, param1, param2):
            # code
            pass

        @staticmethod
        def stc_method(param1, param2):
            # code
            pass


player5 = PlayerCharacter("Mari", 100)

print(player5.return_self)
print(player5.return_self().return_self().return_self())

# 4 pillars of OOP
# 1. encapsulation: binding of data and functions that manipulate that data
# 2. abstraction: hiding of data, ie. only giving access to data that is necessary

# player1.shout("lakdsjflksjf") -> shout method is an abstraction because I just want to use it for a purpose
# list.count() -> count() method is an abstraction because I just want to use it for a purpose
# len(list) -> len() function is an abstraction because I just want to use it for a purpose
# I don't exactly care how shout is implemented

player1.shout("jojojojojojo")
# player1.shout = "BOOOOOO"  # it's possible to override class method -> not good
# player1.shout("jojojojojojo")

print(player1.shout)

# private vs public variables
# can I have private variables? -> NO, use _ underscore to denote private variables as a convention

# 3. inheritance: allows new objects to take on properties of existing objects

"""
# parent class
class User:
    def sign_in(self):
        print("logged in")

    # default attack method will be overwritten by the subclasses attach method implementation
    def attack(self):
        print("do nothing")


# sub-class, child-class, derived class
class Wizard(User):
    def __init__(self, name, special_power):
        self._name = name
        self._special_power = special_power

    def attack(self):
        print(f"attacking with power of {self._special_power}")


# extend class to a parent class by using the parent class as a class parameter
class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        # if we want to call the User.attack() method from the parent class in a sub-class
        User.attack(self)
        self._num_arrows -= 1
        print(f"attacking with arrow. arrows lef: {self._num_arrows}")


wizard1 = Wizard("markus", "blizzard")
print(wizard1)
archer1 = Archer("markus", 23)
print(archer1)

wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()
print(archer1._num_arrows)


# isinstance(instance, Class)

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
# print(isinstance(wizard1, object))  # True wizard1 is a sub-class of the python object base class

# 4. polymorphism: polymorphism means many-forms,
# refers to the way in which object classes can share the same method name,
# but the method names can act differently based on which object calls them

# wizard1.attack()
# archer1.attack()


def player_attack(character):
    # the same method can be called on different object classes, which will alter the resulting output -> polymorphism
    character.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
"""

# exercise: pets
class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Sally(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Peter(Cat):
    def sing(self, sounds):
        return f"{sounds}"


simon = Simon("simon", 1)
sally = Sally("sally", 2)
peter = Peter("peter", 3)

# 1 Add nother Cat

# 2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [simon, sally, peter]
my_cats = [Simon("Simon", 4), Sally("Sally", 21), Peter("Peter", 1)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)


# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()


# super()

"""
# parent class
class User(object):
    def __init__(self, email):
        self._email = email

    def sign_in(self):
        print("logged in")

    # default attack method will be overwritten by the subclasses attach method implementation
    def attack(self):
        print("do nothing")


# sub-class, child-class, derived class
class Wizard(User):
    def __init__(self, name, special_power, email):
        # User.__init__(self, email) # call init method of User inside of sub-class
        super().__init__(
            email
        )  # same as line above, but ommits the need to call User with self
        self._name = name
        self._special_power = special_power

    def attack(self):
        print(f"attacking with power of {self._special_power}")


# extend class to a parent class by using the parent class as a class parameter
class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        # if we want to call the User.attack() method from the parent class in a sub-class
        User.attack(self)
        self._num_arrows -= 1
        print(f"attacking with arrow. arrows lef: {self._num_arrows}")


wizard1 = Wizard("markus", "blizzard", "markus@gmail.com")
print(wizard1._email)
archer1 = Archer("markus", 23)

# introspection -> determine type of object at runtime

wizard2 = Wizard("markus", "rocks", "markus@jo.com")
print(dir(wizard2))
print(dir(archer1))
"""

# dunder __dunder__ / magic methods


class Toy:
    my_dict = {"name": "yoyo", "has_pets": False}

    def __init__(self, color, age):
        self._color = color
        self._age = age

    def __str__(self):
        return f"{self._color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yess???"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])
# print(str("action_figure"))


# exercise: extending list


class SuperList(list):
    # def __init__(self, *args):
    #     print(12323, args)
    #     super().__init__(args)

    def __len__(self):
        return 1000


# super_list1 = SuperList((12, 23, 34))
super_list1 = SuperList([12, 23, 34])

print(super_list1)
super_list1.append(5)
print(super_list1)
print(len(super_list1))

# list1 = list((1, 2, 3))
list1 = list([1, 2, 3])

print(list1)
# issubclass(SubClass, ParentClass)
print(issubclass(SuperList, list))  # check if class is sub-class of parent class
print(issubclass(list, object))

# multiple inheritance - with great power comes great responsibility

# parent class
class User(object):
    def sign_in(self):
        print("logged in")


# sub-class, child-class, derived class
class Wizard(User):
    def __init__(self, name, special_power):
        self._name = name
        self._special_power = special_power

    def attack(self):
        print(f"attacking with power of {self._special_power}")


# extend class to a parent class by using the parent class as a class parameter
class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        self._num_arrows -= 1
        print(f"attacking with arrow. arrows lef: {self._num_arrows}")

    def run(self):
        print("ran really fast")

    def check_arrows(self):
        print(f"{self._num_arrows} remaining")


wizard1 = Wizard("markus", "blizzard")
archer1 = Archer("markus", 23)


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("borgie", "rock-smash-magic", 500)

hb1.attack()
hb1.check_arrows()
hb1.sign_in()

# MRO - method resolution order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(C, B):
    pass


print(D.mro())


class X:
    pass


class Y:
    pass


class Z:
    pass


class A1(X, Y):
    pass


class B1(Y, Z):
    pass


class M(B1, A1, Z):
    pass


# M -> B1 -> A1 -> X -> Y -> Z -> object

print(M.__mro__)  # you can use mro() function or dunder method to determine MRO
# mro() uses depth-first-search to determine the order of method resolution