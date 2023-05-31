#Problem 14

def duplicate(one):
    duplicated_list = []
    for i in range (0,len(one)):
        duplicated_list.extend([one[i],one[i]])
    
    return duplicated_list

example_list = ['a', 'b', 'b', 'c', 'b', 'd']
final_list = duplicate(example_list)
print(final_list)
