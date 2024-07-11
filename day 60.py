#LCM of a Number using Recursion in Python
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def lcm(a, b):
    return (a * b) // hcf(a, b)


first = 23
second = 69

print("Lcm of", first, "and", second, "is", lcm(first, second))