#Power of a Number using Recursion in Python
def power(a, b):
    if b != 0:
        return a * power(a, b - 1)
    else:
        return 1


a = 2
b = 3
print(a, "to the power", b, "is", power(a, b))