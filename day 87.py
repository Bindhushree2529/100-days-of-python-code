#Find maximum product sub-array in a given array
def maxSubarrayProduct(arr, n):
 
    # Initializing result
    result = arr[0]
 
    for i in range(n):
     
        mul = arr[i]
       
        # traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]
         
        # updating the result for (n-1)th index.
        result = max(result, mul)
     
    return result
 
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))