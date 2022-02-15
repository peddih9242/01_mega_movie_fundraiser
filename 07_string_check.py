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

# valid inputs for each snack
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

snack_ok = 0
snack = 0

for item in range(0, 3):

    desired_snack = input("Snack: ").lower()
    
    for var_list in valid_snacks:

        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"
    
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid choice")