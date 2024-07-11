#Find the Longest Palindrome in an Array using Python
# Function to check if n is palindrome
def isPalindrome(n):

   divisor = 1
   while (int(n / divisor) >= 10):
      divisor *= 10

   while (n != 0):
      leading = int(n / divisor)
      trailing = n % 10
  
      if (leading != trailing):
        return False

      n = int((n % divisor) / 10)

      divisor = int(divisor / 100)
   return True

# Function to find the largest palindromic element
def largestPalindrome(arr, n):
   currentMax = -1

   for i in range(0, n, 1):
      if (arr[i] > currentMax and isPalindrome(arr[i])):
         currentMax = arr[i]

   return currentMax

# Driver Code

arr = [1, 232, 5545455, 909090, 161]
n = len(arr)

# print required answer
print(largestPalindrome(arr, n))