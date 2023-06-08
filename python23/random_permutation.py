#Problem 25

import random 

def random_permutation(one):

    return random.sample(one, len(one))


example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
final_list = random_permutation(example_list)
print(final_list)