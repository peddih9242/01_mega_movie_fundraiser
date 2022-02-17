import re

test_strings = [
    "Popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ"
]

# check if item starts with a number
for item in test_strings:
    number_regex = "^[1-9]"

    # separate number and snack in string and get each
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]
    
    else:
        amount = 1
        desired_snack = item

        # remove whitespace
        desired_snack = desired_snack.strip()

    print("Amount: ", amount)
    print("Snack: ", desired_snack)