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

# initialize ticket cost list, valid options and price
ticket_costs = [7.5, 10.5, 10.5, 10.5, 6.5]

payment_options = [
    ["cash", "coins"],
    ["credit", "card", "debit card", "credit card"]
]

# start loop for hard coded test data
for price in ticket_costs:
    
    # get payment method
    payment = "invalid choice"
    while payment == "invalid choice":
        payment = input("What payment method would you like to use? ")
        check_payment = string_checker(payment, payment_options)
    
    # decide whether to have surcharge then add surcharge
    if check_payment == "Credit":
        surcharge = price * 0.05
    else:
        surcharge = 0
    sub_total = price + surcharge
    print("Price: ${:.2f}, Surcharge: ${:.2f}, Original Cost: ${:.2f}".format(sub_total, surcharge, price))
    print()
