# start loop

name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:
    print("You have {} seats left".format(max_tickets - count))
    # get name
    name = input("Name? ")
    count += 1
if count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You sold {} tickets. \n"
    "There are {} places still available.".format(count, max_tickets - count))
