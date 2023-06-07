#Problem 21

def insert_element(one, element, n):

    new_list = []

    for i in range (len(one)):
        new_list.append(one[i])
        if i == (n-2) :
            new_list.append(element)

    return new_list


example_list = ['a', 'b', 'c', 'd', 'e', 'f']

element = input("Enter an element : ")
position = int(input("Enter which position to add the element : "))
final_list = insert_element(example_list, element, position)
print(final_list)