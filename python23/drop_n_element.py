#Problem 16

def drop_element(one, n):

    new_list = []
    count = 1

    for i in range(0,len(one)):

        if count%n != 0:

            new_list.append(one[i])
    
        count = count + 1
    
    return new_list


example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
num = int(input("Enter a value for n : "))
final_list = drop_element(example_list, num)
print(final_list)