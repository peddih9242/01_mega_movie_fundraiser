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

# valid inputs for each snack
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

snack_order = []

check_snack = "invalid choice"
while check_snack == "invalid choice":
    # ask if user wants to order snacks
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)

if check_snack == "Yes":
    desired_snack = ""
    while desired_snack != "xxx":
        desired_snack = input("Snack: ").lower()
        # if user enters the exit code then exit loop
        if desired_snack == "xxx":
            break
        # ask for the desired snack and add snack to list
        snack_choice = string_checker(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

print()
# if they say no to snacks show they ordered none
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    # print ordered snacks
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)