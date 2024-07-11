#HCF of a Number Using Recursion in Python
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


first = 23
second = 69

print('HCF of', first, 'and', second, 'is', hcf(first, second))