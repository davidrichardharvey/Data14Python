# FOR LOOPS
dict_data = {
    1: {"name": "Alex", "animal": "all dogs"},
    2: {"name": "Ben", "animal": "flamingo"},
    3: {"name": "Evie", "animal": "gorilla"},
    4: {"name": "Charlotte", "animal": "giraffe"}
}

for key in dict_data:
    for inner_key in dict_data[key]:
        print(dict_data[key][inner_key])


for key in dict_data:
    print(f"{dict_data[key]['name']}'s favourite animal is {dict_data[key]['animal']}")


# Chinese Menu

chinese_menu = {
    101: {'dish': 'egg fried rice', 'price': 1.60},
}
x = 101
print(f"The {chinese_menu[x]['dish']} costs £{chinese_menu[x]['price']:.2f}")