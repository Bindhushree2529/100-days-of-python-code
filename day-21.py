#Strong Number Program 
#Using Iteration
n =145
#save the number in another variable
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10): #precomputing the factorial value from 0 to 9 and store in the array.
    f[i]=f[i-1]*i

#Implementation
while(temp):
    r=temp%10 #r will have the vale u of the unit digit
    temp=temp//10
    sum+=f[r] #adding all the factorial

if(sum==n):
    print("Yes", n ,"is strong number")

else:
    print("No" , n, "is not a strong number")