#Problem 6

def palindrome(one):

    check_palindrome = True

    for i in range (len(one)//2):
        if one[i] != one[len(one)-i-1]:
           check_palindrome = False

    return check_palindrome


example_list = ['r', 'b', 'c', 'b', 'r']

value = palindrome(example_list)

if value == True:
    print("Palindrome")

else:
    print("Not Palindrome")