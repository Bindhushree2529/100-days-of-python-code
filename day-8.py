#Check Whether a Year is a Leap Year or Not in Python
year = 2000

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")