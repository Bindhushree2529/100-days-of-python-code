#Finding the frequency of element Frequency of elements in an array using Python
# Time Complexity : O(n^2)
# Space Complexity : O(1)

def countFrequency(arr, size):

    for i in range(0, size):
        flag = False
        count = 0

        for j in range(i+1, size):
            if arr[i] == arr[j]:
                flag = True
                break

        # The continue keyword is used to end the current iteration 
        # in a for loop (or a while loop), and continues to the next iteration.
        if flag == True:
            continue

        for j in range(0, i+1):
            if arr[i] == arr[j]:
                count += 1

        print("{0}: {1}".format(arr[i], count))


# Driver Code
arr = [5, 8, 5, 7, 8, 10]
n = len(arr)
countFrequency(arr, n)