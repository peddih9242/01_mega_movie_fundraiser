def num_check(question, low, high):
    
    error = "Please enter a whole number between {} and {}".format(low, high)

    # start loop
    valid = False
    while valid is not True:
        try:
            # get number
            response = int(input(question))
            # check response is valid
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

age = num_check("Age? ", 12, 130)