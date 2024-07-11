#Python Program for Sum Of Two Prime Numbers
# take input
Number = int(input('Enter the Number : '))
# initialize an array
arr = []
# find prime numbers
for i in range(2, Number):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    # append prime numbers to array
    if flag == 0:
        arr.append(i)
# possible combinations
flag = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # if condition is True Print numbers
        if arr[i] + arr[j] == Number:
            flag = 1
            print(str(arr[i]) + " and " + str(arr[j]) + ' are prime numbers when added gives ' + str(Number))
            break
if flag == 0:
    print('No Prime numbers can give sum of ' + str(Number))