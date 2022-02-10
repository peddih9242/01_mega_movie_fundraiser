def not_blank(question, error):
    loop = True
    while loop is not False:
        response = input(question)
        if response == "":
            print(error)
        else:
            return response
            
# Main routine

name = not_blank("What's your name? ", "Sorry, you can't leave this blank - please enter your name.")
