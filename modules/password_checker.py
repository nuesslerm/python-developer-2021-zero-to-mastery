# at least 8 chars long
# needs to contain letters, numbers and symbols $%#@

import re

# regex = r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$"
# lookahead is required to ensure that the password contains the characters in the lookahead
# otherwise the password would still match if e.g. no digit is present
pattern = re.compile(r"^(?=.*[\d])(?=.*[a-z])(?=.*[$%#@])[\w\d$%#@]{8,}\d$")

while True:
    password = input("Enter a good password: ")
    passwordlen = len(password)

    if pattern.fullmatch(password):
        print("password is fine")
        break
    elif passwordlen < 8:
        print(
            f"your password is only {passwordlen} chars long.\n"
            + "password needs to be longer than 8 chars"
        )
    else:
        print(
            "password needs to contain at least 1 letter, 1 number and 1 special symbol from $%#@\n"
            + "password also needs to end with a number"
        )
