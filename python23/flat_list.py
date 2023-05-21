#Problem 7

def flatten(one): 

    flat_list = []
    for item in one:
        if isinstance(item, list):
            flat_list.extend(flatten(item))

        else:
            flat_list.append(item)
    
    return flat_list


example_list = ['a', ['b', ['c', ['i'],'d'], 'e', 'f'], 'g', 'h']
flattened_list = flatten(example_list)
print(flattened_list)