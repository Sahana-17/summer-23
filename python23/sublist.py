#Problem 9

def new_list(one):

    sublist = []
    new_list = []

    for i in range(len(one)):

        if i == 0 or (one[i] != one[i-1]):
            if sublist:
                new_list.append(sublist)
                sublist = []

        sublist.append(one[i])
    
    if sublist:
        new_list.append(sublist)

    return new_list

example_list = ['a', 'a', 'a', 'b', 'b', 'c', 'b', 'b', 'd']
final_list = new_list(example_list)
print(final_list)
