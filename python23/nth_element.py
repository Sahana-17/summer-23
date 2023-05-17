#Problem 3

def find_element(one, n):
    if n < len(one):
        return one[n-1]
    else:
        return None
        

example_list = ['a', 'b', 'c', 'd', 'e']
term = int(input("Enter n : "))

nth_element = find_element(example_list, term)

print("Element : ", nth_element)

