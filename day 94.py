#Python program for rotation of elements of array- left and right
#Write a program for array rotation in Python

# Python3 program to rotate an array by
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
 
# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp
         
 
# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")
 
  
# Driver program to test above functions */
arr = [10, 20, 30, 40, 50, 60, 70]
leftRotate(arr, 2, 7)
printArray(arr, 7)