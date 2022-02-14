def yes_no(question):
    error = "Please enter yes / no"
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)

# main routine

snacks = yes_no("Do you want snacks? ")