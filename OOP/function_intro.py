# # Don't
# # Repeat
# # Yourself
#
# def print_something():
#     print("Something!")
#
# print_something()
# print_something()
# print_something()
#
#
def print_something_multiple(some_string, number_of_times):
    string_to_print = some_string * number_of_times
    print(string_to_print)
#
# print_something_multiple("Woohoo!", 3)
#
# print_something_multiple("6", 3)

def repeat_string(string_to_repeat: str, number_of_repeats: int = 3) -> str:
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return

repeat_string("Woohoo")


#
#
# print(repeat_string(number_of_repeats=5))
# print(repeat_string("Woohoooooo", 17))

# Given a tuple of numbers numbers
# Set up a current product tracker
# Iterate through each number
# Multiple current product by number
# Return the number

