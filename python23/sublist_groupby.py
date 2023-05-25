#Problem 9 alternate solution using groupby

from itertools import groupby

def pack(sample_list):
    sublist = []
    for key, group in groupby(sample_list):
         sublist.append(list(group))

    return sublist

example_list = ['a', 'a', 'a', 'b', 'b', 'c', 'b', 'b', 'd']
print(pack(example_list))