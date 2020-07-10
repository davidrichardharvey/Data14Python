

age_input = ""

while not age_input.isnumeric():
    age_input = input("Enter your age:\n")
    if not age_input.isnumeric():
        print("That's not a number, try again")

age = int(age_input)

print("You are " + str(age))