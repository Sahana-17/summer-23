#Problem1

def find_element(one):

    if not one:
        return None
    else:
        return one[-1]
    

example_list = ['a', 'b', 'c', 'd']
last_element = find_element(example_list)

print("Last element : ", last_element)

