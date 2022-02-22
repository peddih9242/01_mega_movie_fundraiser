from os import O_RANDOM
import pandas

# initialize lists

popcorn = []
pita_chips = []
water = []
orange_juice = []
mnms = []

count = 0

snack_list = [popcorn, mnms, pita_chips, water, orange_juice]

snack_dict = {
    'Popcorn:': popcorn,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice,
    'M&Ms': mnms
}

names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]

test_data = [

[[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
[[]],
[[1, 'Water']],
[[1, 'Popcorn'], [1, 'Orange Juice']],
[[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

# get order

for client_order in test_data:
    
    for item in snack_list:
        item.append(0)
    
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        # make sure order is not blank, get amount and item
        # and add to list
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = snack_dict[to_find]
            add_list[-1] = amount

print()
print("Popcorn: ", snack_list[0])
print("M&Ms:", snack_list[1])
print("Pita Chips", snack_list[2])
print("Water", snack_list[3])
print("Orange Juice", snack_list(4))