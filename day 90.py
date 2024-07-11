#Finding Sum of Minimum Absolute Difference of Array using Python
#Write a program to find the sum of minimum absolute difference using python
import sys

def sumOfMinAbsDifferences(arr,n):
    result = sys.maxsize
    
    for i in range(0,n):
        sum = 0;
        for j in range(0, n):
            sum += abs(arr[i]-arr[j])
        result = min(result, sum)
    return result;
         
 
# Driver code
arr = [2, 5, 4, 3]
n = len(arr)
print( "Required Sum = ", sumOfMinAbsDifferences(arr, n))