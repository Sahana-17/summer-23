#Problem 31

def is_prime(n):

    if n < 2:  
        return False

    for i in range(2, n):

        if n % i == 0:  
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Composite")
