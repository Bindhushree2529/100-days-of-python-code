#Find the sum of the Digits of a Number
num = 12345
sum = 0

while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10

print(sum)