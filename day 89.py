#Determine can all numbers of an array be made equal in Python
#Function to check whether an array is equal or not
def check(array,length):
     for i in range(0, length):
     
          # Divide number by 2
            while array[i] % 2 == 0:
                array[i] //= 2

          # Divide number by 3
            while array[i] % 3 == 0:
                array[i] //= 3

     if array[i] != array[0]:
         return False

     return True

#input array from user
array = [50, 100, 75]

#determine length of array and assign to length variable
length=len(array)

if check(array, length):
     print("Yes, all the elements of an array can be made equal")
else:
     print("No, all the elements of an array cannot be made equal")