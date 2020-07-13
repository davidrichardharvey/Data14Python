

age_input = ""
age_verify = False
while not age_verify:
    age_input = input("Enter your age:\n")
    if len(age_input) <= 3 and age_input.isnumeric():
        age_verify = True
    # if not age_input.isnumeric():
    #     print("That's not a number, try again")

age = int(age_input)

print("You are " + str(age))