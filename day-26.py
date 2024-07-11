# check Abundant Number
n = 12

sum=1 # 1 can divide any number 

for i in range(2,n):
  if(n%i==0):    #if number is divisible by i add the number 
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')