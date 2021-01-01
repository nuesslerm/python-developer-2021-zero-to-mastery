# error handling for build-in exceptions
# e.g. TypeError, IndexError (out-of-bounds), KeyError, ZeroDivisionError, ValueError


def what():
    while True:
        try:
            age = int(input("what is your age? "))
            if age < 0:
                raise Exception("please enter an age higher than 0")
            print(f"bruh 10 divided by your age is {10/age}")
        except ValueError:
            print("please enter a number")
            # continue
        except ZeroDivisionError:
            print("no 0 allowed")
            # break
        except Exception as err:
            print(err)
        else:  # executes when try-block executes successfully
            print("yay. you didn't have an exception!")
            break
        # finally:
        #     print("ok, I am finally done")


what()


"""
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"please enter two numbers\n{err}")


print(sum(1, 0))
"""