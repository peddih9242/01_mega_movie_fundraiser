import pandas

first_list = ["a", "b", "c"]
second_list = ["z", "y", "x"]

dictionary = {
    'First one': first_list,
    'Second one': second_list
}

printframe = pandas.DataFrame(dictionary)
print(printframe)