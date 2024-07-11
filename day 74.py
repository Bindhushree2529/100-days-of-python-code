#Python Code for Reverse an Array
def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)