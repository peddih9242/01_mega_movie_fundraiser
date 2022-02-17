# valid inputs for each snack
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

snack_ok = 0
snack = 0

# loop for testing
for item in range(0, 3):

    desired_snack = input("Snack: ").lower()
    
    # check for valid inputs in each list
    for var_list in valid_snacks:

        # print first word in list of valid input
        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"
    
    # output snack choice
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid choice")