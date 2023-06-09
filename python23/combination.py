#Problem 26

from itertools import combinations

def combination(one, n):
    
    return list(combinations(one, n))


num = 3
example_list = ['a', 'b', 'c', 'd', 'e', 'f']
combinations = combination(example_list, num)

for comb in combinations:
    print(comb)
