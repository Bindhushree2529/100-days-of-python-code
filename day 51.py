#Program to count the Occurrence of a Digit in a given Number in Python
def countOccurrances(n, d):
    count = 0
 
    # Loop to find the digits of N
    while (n > 0):
 
        # check if the digit is D
        if(n % 10 == d):
            count = count + 1
  
        n = n // 10
 
    return count
 
# Driver code
d = 2
n = 828282
print(countOccurrances(n, d))