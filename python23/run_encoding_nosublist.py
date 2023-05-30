#Problem 13 (similar to no sublist version of problem 10

def run_encoding(one):

    encoded_list = []
    count = 1

    for i in range(1, len(one)):
        if one[i] == one[i-1]:
            count += 1
        else:
            encoded_list.append([count, one[i-1]])
            count = 1

    encoded_list.append([count, one[i-1]])
    return encoded_list


example_list = ['a', 'b', 'a', 'a', 'b', 'b', 'c', 'b', 'b', 'd']
final_list = run_encoding(example_list)
print(final_list)