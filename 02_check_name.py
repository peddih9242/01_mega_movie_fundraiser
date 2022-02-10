def not_blank(question):
    loop = True
    while loop is not False:
        response = input(question)
        if response == "":
            print("Sorry - this can't be blank")
        else:
            return response
            
# Main routine

name = not_blank("What's your name? ")
