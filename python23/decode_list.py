#Problem 12

def decode(one):
    decoded_list = []

    for item in one:
        if isinstance(item, list):
            count = item[0]
            element = item[1]
            for i in range(0,count):
                decoded_list.extend(element)
        else:
            decoded_list.append(item)

    return decoded_list

encoded_list = [[3, 'a'], [2, 'b'], 'c', [2, 'b'], 'd']
decoded_list = decode(encoded_list)
print(decoded_list)
