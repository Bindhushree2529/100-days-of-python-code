# Binary To Decimal Conversion
num = 10
binary_val = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {}\nDecimal Number is {}".format(binary_val, decimal_val))