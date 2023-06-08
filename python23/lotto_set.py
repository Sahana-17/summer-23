#Problem 24

import random

def lotto_set(n, r):

    return random.sample(range(r), n)


num = int(input("Enter number of values to add to list : "))
range_value = int(input("Enter a value for range : "))
final_list = lotto_set(num, range_value)
print(final_list)