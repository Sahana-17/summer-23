#Problem 2

def find_element(one):
    if len(one) < 2:
        return None
    
    return one[-2]
    

example_list = ['a', 'b', 'c', 'd']
second_last_element = find_element(example_list)

print("Second Last Element : ", second_last_element)

