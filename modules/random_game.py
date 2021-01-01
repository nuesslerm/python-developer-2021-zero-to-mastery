from sys import argv, exit
from random import randint


argv_len = len(argv[1:])

if argv_len > 2:
    print("Please enter a max of two numbers after the script name")
    exit()

try:
    first_num = int(argv[1] if argv_len > 0 else 0)
    second_num = int(argv[2] if argv_len > 1 else 10)
except ValueError:
    print("Please enter only integers for script args!")
    exit()


while True:
    answer = input(f"Guess an integer between {first_num} and {second_num} ")

    try:
        if float(answer) % 1 != 0:
            print("Please enter an integer")
            continue

        to_guess = randint(first_num, second_num)
        guess = int(answer)

        if to_guess == guess:
            print("Congrats. You got the number right!")
            break
        else:
            print("Sorry. The number is wrong. Try again!")
            continue
    except ValueError:
        print("Please enter an integer")
        continue