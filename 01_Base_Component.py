# import statements

# functions

# check that ticket name is not blank
def not_blank(question, error):
    loop = True
    while loop is not False:
        response = input(question)
        if response == "":
            print(error)
        else:
            return response

# main routine

# ask if user has used the program befre

# loop to get ticket details

name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:
    print("You have {} seats left".format(max_tickets - count))
    # get name (deny blank)
    name = not_blank("What's your name? ", "Sorry, you can't leave this blank - please enter your name.")
    count += 1
if count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You sold {} tickets. \n"
    "There are {} places still available.".format(count, max_tickets - count))

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necessary)

# calculate total sales and profit

# output data to text file