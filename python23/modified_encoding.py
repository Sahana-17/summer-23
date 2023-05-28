#Problem 11

def run_encoding(one):
    encoded_list = []
    count = 1

    for i in range(1, len(one)):
        if one[i] == one[i - 1]:
            count = count + 1
        else:
            if count > 1:
                encoded_list.append([count, one[i - 1]])
            else:
                encoded_list.append(one[i - 1])
            count = 1

    if count > 1:
        encoded_list.append([count, one[i]])

    else:
        encoded_list.append(one[i])

    return encoded_list


example_list = ['a', 'a', 'a', 'b', 'b', 'c', 'b', 'b', 'd']
final_list = run_encoding(example_list)
print(final_list)