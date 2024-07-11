#Python Program to count the number of days in a given month of a year
month = 12
year=2012
    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29");

elif(month==2) :
    print("Number of days is 28");

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31");

else :
    print("Number of days is 30");