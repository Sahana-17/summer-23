#Problem 19 (works only for positive value of n)

def rotate_list(one,n):

    list_1 = []
    list_2 = []
    new_list = []

    for i in range(len(one)):
         
        if i < n:
            list_1.append(one[i])
        else:
            list_2.append(one[i])

        new_list = list_2 + list_1

    return new_list

example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

num = int(input("Enter a value for n : "))
final_list = rotate_list(example_list, num)

print(final_list)