# добавление элемента в список

# классика
def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
        input_list.append(2)

    return input_list


result = add_to_list([1, 4, 5])
print(result)
result = add_to_list()
print(result)
print('# через or /////////////////////:')
def add_to_list(input_list=None):

    input_list = input_list or   []
    input_list.append(2)

    return input_list


result = add_to_list([1, 4, 5])
print(result)
result = add_to_list()
print(result)
