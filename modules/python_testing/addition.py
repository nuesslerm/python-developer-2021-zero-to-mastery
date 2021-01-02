# def do_stuff(num, num2, num3):
#     return num + num2 + num3 + 5


def do_stuff(num=0, num2=0, num3=0):
    try:
        num = num if num != None else 0
        num2 = num2 if num2 != None else 0
        num3 = num3 if num3 != None else 0

        return int(num) + int(num2) + int(num3) + 5
    except ValueError as err:
        return err


# do_stuff(None, 1, 2)
# print(type(None))

# print("hoooo")

# pythong scope rule: LEGB - local, enclosing, global, built-in