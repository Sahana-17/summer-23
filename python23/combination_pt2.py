#Problem 26 without importing itertools

def combination(one, n):
    if n == 0:
        yield []
    elif len(one) < n:
        return
    else:
        first, *rest = one
        for comb in combination(rest, n-1):
            yield [first] + comb
        yield from combination(rest, n)


num = 3
example_list = ['a', 'b', 'c', 'd', 'e', 'f']
combinations = list(combination(example_list, num))

for comb in combinations:
    print(comb)