#Interview question - Find index of pair that have a sum of target

def find_pair(num, target):

    pair_list = []
    
    for i in range(1, len(num)):
        for j in range(1, len(num)):
            if (num[i] + num[j]) == target:
                pair_list.append(i)

    return pair_list

nums = [3, 1, 2, 6, 7, 4]
target = 6
result = find_pair(nums, target)
print(result)
