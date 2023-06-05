#Problem 18

def slice_list(one, i, k):

    new_list = []
    count = 1

    for j in range(len(one)):

        if count >= i and count <= k:
            print(count)
            new_list.append(one[j])

        count = count + 1
    return new_list


example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

start = int(input("Enter the start index : "))
end = int(input("Enter the end index : "))

final_list = slice_list(example_list, start, end)
print(final_list)