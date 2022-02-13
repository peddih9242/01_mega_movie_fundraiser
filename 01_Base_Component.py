# import statements

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

# main routine

# ask if user has used the program befre

# loop to get ticket details

name = ""
count = 0
max_tickets = 5
ticketprofit = 0

while name != "xxx" and count < max_tickets:
    print("You have {} seats left".format(max_tickets - count))
    # get name (deny blank)
    name = not_blank("What's your name? ", "Sorry, you can't leave this blank - please enter your name.")
    # end loop if the exit code is entered
    if name == "xxx":
        break

    # get age (between 12 and 130)
    age = num_check("Age? ")

    if age < 12:
        print("Sorry you are too young")
        print()
        continue
    elif age > 130:
        print("That is probably a mistake!")
        print()
        continue
    count += 1
    print()

    # calculate ticket price
    if age < 16:
        price = 7.5
    elif age >= 65:
        price = 6.5
    else:
        price = 10.5
    # calculate profit
    profit = price - 5
    ticketprofit += profit

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