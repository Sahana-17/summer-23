#Problem 8

def duplicate(one):

    eliminated_list = []

    for i in range(len(one)):
        if i == 0 or (one[i] != one[i-1]):
            eliminated_list.append(one[i])
        
    return eliminated_list


example_list = ['a','a','a','c','b','a','a','d']

final_list = duplicate(example_list)
print(final_list)