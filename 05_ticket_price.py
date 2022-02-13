valid = False
totalprofit = 0
# loop
while not valid:
    # get age and set appropriate price for the age
    age = int(input("age: "))
    if age == -1:
        break
    elif age < 16:
        price = 7.5
    elif age >= 65:
        price = 6.5
    else:
        price = 10.5
    # calculate profit
    profit = price - 5
    totalprofit += profit

# show total profit made
print("Total profit: ${:.2f}".format(totalprofit))