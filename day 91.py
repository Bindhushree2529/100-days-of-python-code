#Python Program to Sort Array according to the order defined by Another Array
from collections import Counter

def solve(arr1, arr2):
    res = []
    
    f = Counter(arr1)
     
    for e in arr2:
       
        res.extend([e]*f[e])
         
        f[e] = 0
         
    rem = list(sorted(filter(lambda x: f[x] != 0, f.keys())))
     
    for e in rem:
        res.extend([e]*f[e])
         
    return res
 
 
# Driver Code
arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ];
arr2 = [ 20, 1, 18, 39 ];
print(*solve(arr1, arr2))