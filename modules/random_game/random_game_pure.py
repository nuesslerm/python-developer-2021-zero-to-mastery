from sys import argv, exit
from random import randint


def assess_string_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def assess_string_to_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def check_for_errors_on_script_start(args):
    args_len = len(args[1:])

    if args_len > 2:
        print("Please enter a max of two numbers after the script name")
        return True
    for item in args:
        if assess_string_to_int(item):
            print("Please enter only integers for script args!")
            return True
    return False


def check_for_errors_on_guess(float_input, first_num, second_num):
    if float_input % 1 != 0:
        print("Please enter an integer")
        return True
    if not first_num <= float_input <= second_num:
        print("Your guess is out of bounds of the guessing range")
        return True
    return False


def get_numbers(args):
    args_len = len(args[1:])

    first_num = int(args[1]) if args_len > 0 else 0
    second_num = int(args[2]) if args_len > 1 else 10

    return (first_num, second_num)


def get_rand_int(first_num, second_num):
    return randint(first_num, second_num)


def parse_input_to_float(input):
    if assess_string_to_float(input):
        return float(input)
    else:
        print("Please enter an integer")
        return None


def guess_numbers(float_input, to_guess):
    try:
        guess = int(float_input)

        if to_guess == guess:
            print("Congrats. You got the number right!")
            return True
        else:
            print("Sorry. The number is wrong. Try again!")
            return False
    except ValueError:
        print("Please enter an integer")
        return False


def main():
    if check_for_errors_on_script_start(argv):
        exit()

    first_num, second_num = get_numbers(argv)
    to_guess = get_rand_int(first_num, second_num)

    while True:
        answer = input(f"Guess an integer between {first_num} and {second_num}: ")

        float_input = parse_input_to_float(answer)

        if not float_input:
            continue

        if check_for_errors_on_guess(float_input, first_num, second_num):
            continue

        if guess_numbers(float_input, to_guess):
            break
        else:
            continue


if __name__ == "__main__":
    main()