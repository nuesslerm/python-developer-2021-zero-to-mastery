print("Do you deserve christmas shoes? Let's find out!!")

input("Press 'Enter' to continue.")

answer = None

validAnswers = ["y", "Y", "n", "N", ""]

while answer not in validAnswers:
    answer = input("You a pusheen? (y/N)\n")
    pass

if answer == "y" or answer == "Y":
    print("Nooooooooo, f- off 🚧")
    pass
else:
    print("I guess")
    pass
