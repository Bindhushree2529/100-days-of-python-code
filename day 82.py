#Removing Duplicates elements from an array
# This function returns new size of modified array.
def removeDuplicates(arr, n):

    # Return, if array is empty or contains a single element
    if n == 0 or n == 1:
        return n

    # Start traversing elements
    j = 0;
    for i in range(0, n-1):

        # If current element is not equal to next element then store that current element
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]
    j += 1

    return j

# Driver code
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
n = len(arr)

n = removeDuplicates(arr, n)

# Print updated array
for i in range(n):
    print ("%d"%(arr[i]), end = " ")