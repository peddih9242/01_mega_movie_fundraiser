valid = False
while not valid:
    snacks = input("Do you want snacks? ").lower()
    
    if snacks == "yes" or snacks == "no":
        print("You answered yes / no")
    else:
        print("Please answer yes / no")