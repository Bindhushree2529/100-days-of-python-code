#Python Program for sorting elements of an Array by Frequency
from collections import Counter
ini_list = [10, 20, 30, 40, 40, 50, 50, 50]

# sorting on bais of frequency of elements
result = [item for items, c in Counter(ini_list).most_common() for item in [items] * c]

# printing final result
print(str(result))