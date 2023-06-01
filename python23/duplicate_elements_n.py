#Problem 15

def duplicate(one, n):
    duplicated_list = []
    for i in range (0,len(one)):
        duplicated_list.extend([one[i]] * n)
    
    return duplicated_list

example_list = ['a', 'b', 'b', 'c', 'b', 'd']
number = int(input("Enter number of times you wish to duplicate the list : "))
final_list = duplicate(example_list, number)
print(final_list)
