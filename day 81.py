#Find non-repeating elements in an array Python
# Python 3 program to count unique elements
def count(arr, n):

   # Mark all array elements as not visited
   visited = [False for i in range(n)]

   # Traverse through array elements
   # and count frequencies
   for i in range(n):

     # Skip this element if already
     # processed
     if (visited[i] == True):
        continue

     # Count frequency
     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1
     if count == 1 :
        print(arr[i]);
   

# Driver Code
arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)