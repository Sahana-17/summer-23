#Problem 10

def run_encoding(one):

    sublist = []
    encoded_list = []
    count = 1

    for i in range(1, len(one)):

        if (one[i] != one[i-1]):

            sublist.append(count)
            sublist.append(one[i-1])
            
            encoded_list.append(sublist)
            sublist = []
            count = 1
            
        else:
            count = count + 1
    

    sublist.append(count)
    sublist.append(one[-1])
    encoded_list.append(sublist)

    return encoded_list

example_list = ['a', 'a', 'a', 'b', 'b', 'c', 'b', 'b', 'd']
final_list = run_encoding(example_list)
print(final_list)