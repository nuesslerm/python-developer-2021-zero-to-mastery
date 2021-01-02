from sys import argv, exit
from random import randint

# the below code doesn't adhere to the functional programming paradigm,
# in that it is not built with pure functions
# for refactored code refer to file random_game_pure.py

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

to_guess = randint(first_num, second_num)
print(to_guess)

while True:
    try:
        parsed_input = float(
            input(f"Guess an integer between {first_num} and {second_num}: ")
        )
        if parsed_input % 1 != 0:
            print("Please enter an integer")
            continue

        if not first_num <= parsed_input <= second_num:
            print("Your guess is out of bounds of the guessing range")
            continue

        guess = int(parsed_input)
        if to_guess == guess:
            print("Congrats. You got the number right!")
            break
        else:
            print("Sorry. The number is wrong. Try again!")
            continue
    except ValueError:
        print("Please enter an integer")
        continue