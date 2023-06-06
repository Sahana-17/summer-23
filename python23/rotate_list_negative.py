#Problem 19 to ensure both positive and neagtive values of n work

def rotate_list(one,n):

    n = n % len(one) #modulo is used to ensure code works even if n > len(one)
    one = one[n:] + one[:n]

    return one

example_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

num = int(input("Enter a value for n : "))
final_list = rotate_list(example_list, num)

print(final_list)