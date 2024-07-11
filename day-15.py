#Find the Armstrong Numbers between Two Intervals
low, high = 10, 10000

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")