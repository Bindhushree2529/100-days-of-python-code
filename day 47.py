#Python program to find Prime Numbers between 1 to100.
def checkPrime(num):

    #  0, 1 and negative numbers are not prime
    if num < 2:
        return 0
    else:

        # no need to run loop till num-1 as for any number x the numbers in
        # the range(num/2 + 1, num) won't be divisible anyway
        # Example 36 won't be divisible by anything b/w 19-35

        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0

    # the number would be prime if we reach here
    return 1


a, b = 1, 100
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")