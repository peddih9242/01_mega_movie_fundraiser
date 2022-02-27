from http.client import PAYMENT_REQUIRED


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

# main routine

payment_options = [
    ["cash", "coins"]
    ["credit", "card", "debit card", "credit card"]
]

payment = "invalid choice"
while payment == "invalid choice":
    payment = input("What payment method would you like to use? ")