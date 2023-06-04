#Problem 17

def split_list(one, n):

    list_1 = []
    list_2 = []
    for i in range(len(one)):
        if i < n:
            list_1.append(one[i])
        else:
            list_2.append(one[i])
    
    return list_1, list_2





example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
num = int(input("Enter a value for n : "))
final_list_1, final_list_2 = split_list(example_list, num)
print("List 1 : ", final_list_1)
print("List 2 : ", final_list_2)
