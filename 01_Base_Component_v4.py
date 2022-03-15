# import statements

import pandas
import re

# functions

# string checker, checks for valid input from multiple lists
def string_checker(choice, options):
    
    # check for valid input in each list
    for var_list in options:

        # look for valid input in each list
        if choice in var_list:
            chosen = var_list[0].title()
            valid = "yes"
            break
        else:
            valid = "no"
    if valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


# check that ticket name is not blank
def not_blank(question, error):
    loop = True
    while loop is not False:
        response = input(question)
        if response == "":
            print(error)
            print()
        else:
            return response


# number checking function, checks for integer above 0
def num_check(question):

    error = "Please enter a whole number above 0."

    # start loop
    valid = False
    while valid is not True:
        try:
            # get number
            response = int(input(question))
            # check response is valid
            if response >= 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# ask for ticket age, look for invalid age and calculate ticket price
def get_ticket_price():

    # get age (between 12 and 130)
    age = num_check("Age? ")

    # check for invalid age input and restart loop if found
    if age < 12:
        print("Sorry you are too young")
        print()
        return "invalid ticket price"
    elif age > 130:
        print("That is probably a mistake!")
        print()
        return "invalid ticket price"
    
    print()

    # calculate ticket price
    if age < 16:
        return 7.5
    elif age >= 65:
        return 6.5
    else:
        return 10.5


# ask if user wants snacks and take in desired snacks
def get_snack():

    # check if item starts with a number
    number_regex = "^[1-9]"

    snack_order = []


    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []

        desired_snack = input("Snack: ").lower()
        if desired_snack == "xxx":
            return snack_order

        # separate number and snack in string and get each
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]        
        else:
            amount = 1

        # remove whitespace
        desired_snack = desired_snack.strip()
        snack_choice = string_checker(desired_snack, valid_snacks)

        if amount > 4:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"
        
        # add amount and choice to lists
        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# surcharge function, calculates surcharge and returns sub total with surcharge
def surcharge():
    # get payment method
    check_payment = "invalid choice"
    while check_payment == "invalid choice":
        payment = input("What payment method would you like to use? ")
        check_payment = string_checker(payment, payment_options)
    
    # decide whether to have surcharge then add surcharge
    if check_payment == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0
    return surcharge_multiplier

# snack analysing function, gets total amount of each snack
def snack_analyser(list):
    # get order
    count = 0
    for client_order in list:
        # make amount of each snack 0
        for item in snack_list:
            item.append(0)
        
        snack_given = list[count]
        count += 1

        for item in snack_given:
            # make sure order is not blank, get amount and item
            # and add to list
            if len(item) > 0:
                to_find = (item[1])
                amount = (item[0])
                add_list = movie_data_dict[to_find]
                add_list[-1] = amount


def currency(x):
    return "${:.2f}".format(x)


def instructions(options):
    want_instructions = "invalid choice"
    while want_instructions == "invalid choice":
        want_instructions = input("Would you like to read the instructions? ")
        check_instructions = string_checker(want_instructions, options)

    if check_instructions == "yes":
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print()
        print("Enter the names, ages and the snacks your group wants.")
        print("This program will calculate the ")
    else:
        return ""

# main routine

# ask if user has used the program before

# loop to get ticket details

# initialise variables

name = ""
count = 0
max_tickets = 150
ticket_profit = 0
ticket_sales = 0

# initialise lists

all_names = []
all_tickets = []
all_snacks = []
surcharge_mult_list = []

popcorn = []
mnms = []
pita_chips = []
water = []
orange_juice = []

store_grand_total = []

snack_list = [popcorn, mnms, pita_chips, water, orange_juice]

# lists to store summary data
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water",
    "Orange Juice", "Snack Profit", "Ticket Profit", "Total Profit"]

summary_data = []

# initialise dictionaries

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice,
    'M&Ms': mnms,
    'Surcharge Multiplier': surcharge_mult_list
}

summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# valid responses for string checker
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

payment_options = [
    ["cash", "coins", "ca"],
    ["credit", "card", "debit card", "credit card", "cr"]
]

valid_snacks = [
    ["popcorn", "p", "pop", "corn", "a"],
    ["M&Ms", "m&m's", "mms", "mm", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "o", "e"]
    ]

instructions(yes_no)

while name != "xxx" and count < max_tickets:
    print("You have {} seats left".format(max_tickets - count))

    # get name (deny blank)
    name = not_blank("What's your name? ", "Sorry, you can't leave this blank - please enter your name.")
    # end loop if the exit code is entered
    if name == "xxx":
        break

    # get price of ticket
    ticket_price = get_ticket_price()
    if ticket_price == "invalid ticket price":
        continue
    
    count += 1

    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)
    
    # get snack and append to list
    snack = get_snack()
    all_snacks.append(snack)

    # get surcharge and append to list
    surcharge_multi = surcharge()
    surcharge_mult_list.append(surcharge_multi)

snack_analyser(all_snacks)

# print details
movie_frame = pandas.DataFrame(movie_data_dict, columns = ['Name', 'Ticket', 'Surcharge Multiplier', 'M&Ms', 'Orange Juice', 'Pita Chips', 'Popcorn', 'Water'])
movie_frame = movie_frame.set_index('Name')

movie_frame["Snack Total"] = \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice'] \

movie_frame["Sub Total"] = movie_frame['Ticket'] \
    + movie_frame['Snack Total']

movie_frame["Surcharge"] = \
    movie_frame['Sub Total'] * movie_frame['Surcharge Multiplier']

movie_frame["Total"] = movie_frame['Sub Total'] \
    + movie_frame['Surcharge']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                            'Pita Chips': 'Chips', 'Surcharge Multiplier': 'SM'})

# set up summary data frame and populate snack items

for item in snack_list:
    # sum items in each snack list
    summary_data.append(sum(item))

# get snack profit
# get snack total from panda
snack_total = movie_frame['Snack Total'].sum()
snack_profit = snack_total * 0.2

# calculate ticket profit and add to list
ticket_profit = ticket_sales - (5 * count)

# get total profit and add to list
total_profit = ticket_profit + snack_profit

dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "${:.2f}".format(item)
    summary_data.append(item)

# summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# set up columns to be printed
pandas.set_option('display.max_columns', None)

# *** Pre Printing / Export ***
# Format currency values so they have $'s

# Ticket Details Formatting (uses currency function)
add_dollars = ['Ticket', 'Snack Total', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

get_total = ['Ticket', 'SM', 'M&Ms', 'OJ', 'Chips', 'Popcorn', 'Water', 'Snack Total', 'Sub Total', 'Surcharge']
for item in get_total:
    movie_frame[item] = ""
movie_frame['Grand Total'] = movie_frame

# write each frame to separate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")


# output the frames
print()
print("*** Ticket / Snack Information ***")
print(movie_frame[['Ticket', 'Snack Total', 'Sub Total', 'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)