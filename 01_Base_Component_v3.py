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
    
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj"]
    ]

    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

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

# main routine

# ask if user has used the program befre

# loop to get ticket details

name = ""
count = 0
max_tickets = 5
ticket_profit = 0
ticket_sales = 0

all_names = []
all_tickets = []


movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# valid responses for yes/no and payment options
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

payment_options = [
    ["cash", "coins"],
    ["credit", "card", "debit card", "credit card"]
]

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

snack = get_snack()

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# calculate profit
ticket_profit = ticket_sales - (5 * count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

if count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You sold {} tickets. \n"
    "There are {} places still available.".format(count, max_tickets - count))
    


    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necessary)

# calculate total sales and profit

# output data to text file