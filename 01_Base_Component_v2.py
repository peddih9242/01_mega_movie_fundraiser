# import statements

import pandas

# functions

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

# string checking function, checks that input is the same
# a valid input (given with list) or first letter of valid input
# for invalid input, give customizable error
def string_checker(question, check_list, error):
    # start loop
    valid = False
    while not valid:
        # get input
        response = input(question).lower()
        # check if response is same as each valid response or first letter
        for item in check_list:
            if response == item or response == item[0]:
                return item
        else:
            print(error)

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