#Problem 20

def remove_element(one,n):

    new_list = []

    for i in range (len(one)):
        if (i+1) != n:
            new_list.append(one[i])
    
    return new_list

example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

num = int(input("Enter a value for n : "))
final_list = remove_element(example_list, num)
print(final_list)