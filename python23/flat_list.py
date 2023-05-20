#Problem 7

def flatten(list): 

    flat_list = []
    for nest_list in example_list:
        for num in nest_list:
            flat_list.append(num)

    print(flat_list)

example_list = [[1, 2], [3], [4, 5, 6, 7]]

flatten(example_list)