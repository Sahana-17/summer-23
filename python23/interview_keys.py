#Interview question without nested list (dictionary)

def find_pair(num, target):

    pair_dict = {}

    for i in range(len(num)):
        number = num[i]

        if target - number in pair_dict:
            return [pair_dict[target - number], i]
        else:
            pair_dict[number] = i

    return []

number_list = [3, 1, 2, 6, 7, 4]
target = 6
result = find_pair(number_list, target)
print(result)
