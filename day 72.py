#Find Second Smallest Element in an Array using Python
import math

arr = [10, 13, 17, 11, 34, 21]
first = math.inf
second = math.inf

for i in range(0, len(arr)):
   if arr[i] < first:
     first = arr[i]

for i in range(0, len(arr)):
   if arr[i] != first and arr[i] < second:
     second = arr[i]

print(second)