import pandas

# initialize lists

popcorn = []
pita_chips = []
water = []
orange_juice = []
mnms = []

count = 0

snack_list = [popcorn, mnms, pita_chips, water, orange_juice]

names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
ticket_price = [7.5, 10.5, 10.5, 10.5, 6.5]

movie_dict = {
    'Name': names,
    'Ticket': ticket_price,
    'Popcorn': popcorn,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice,
    'M&Ms': mnms
}

price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

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
            add_list = movie_dict[to_find]
            add_list[-1] = amount

movie_frame = pandas.DataFrame(movie_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                            'Pita Chips': 'Chips'})

# snack_results.sort_index(axis=0)
print(movie_frame)