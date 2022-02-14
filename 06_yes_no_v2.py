def yes_no(question, check_list):
    error = "Please enter yes / no"
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

valid_strings = ["yes", "no"]

# main routine

snacks = yes_no("Do you want snacks? ", valid_strings)