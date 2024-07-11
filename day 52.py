#Python program to find number of integers which has exactly x divisors
Number = 7
Divisor = 2
#count is to count total number of Numbers with exact divisor
count = 0
#driver loop
for i in range(1,Number+1):
    #count_factors checks the total number of divisors
    count_factors = 0
    #loop to find number of divisors
    for j in range(1,i+1):
        if i % j == 0:
            count_factors += 1
        else:
            pass
    if count_factors == Divisor:
        count +=1

#for break in line between Numbers and total count
print(count)