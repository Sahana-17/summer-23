#Problem 22

def int_list(lower, upper):

    new_list = []
    for i in range (lower, upper+1):
        new_list.append(i)

    return new_list


lower_range = int(input("Enter the lower range : "))
upper_range = int(input("Enter the upper range : "))

integer_list = int_list(lower_range, upper_range)
print(integer_list)