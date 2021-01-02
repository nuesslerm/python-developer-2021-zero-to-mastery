# def do_stuff(num, num2, num3):
#     return num + num2 + num3 + 5


def do_stuff(num, num2, num3):
    try:
        return int(num) + int(num2) + int(num3) + 5
    except ValueError as err:
        return err


# print("hoooo")

# pythong scope rule: LEGB - local, enclosing, global, built-in