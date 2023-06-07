#Problem 23

import random

def random_list (one, n):

    return random.sample(one,n)

example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

num = int(input("Enter a value for n : "))
random_sublist = random_list(example_list, num)
print(random_sublist)