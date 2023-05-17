#Problem 4

def find_element(one):
    if not one:
        return None
    else:
        return len(one)
        

example_list = ['a', 'b', 'c', 'd', 'e']

no_of_elements = find_element(example_list)

print("Number of elements : ", no_of_elements)

