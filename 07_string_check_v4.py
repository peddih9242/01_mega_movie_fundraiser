import re

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


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj"]
]

snack_order = []

# check if item starts with a number

check_snack = "invalid choice"
while check_snack == "invalid choice":
    # ask if user wants to order snacks
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)

# ask for which snack if they want snacks
if check_snack == "Yes":
    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower()
        if desired_snack == "xxx":
            break

        number_regex = "^[1-9]"

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
# if they say no to snacks show they ordered none
if len(snack_order) == 0:
    snack_order.append(None)

print()
print("Snacks Ordered:")
for item in snack_order:
    print(item)

    print(snack_order)