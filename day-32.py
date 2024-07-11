#octal to decimal conversion
def OctalToDecimal(num):
    decimal_value = 0
    base = 1

    while num:
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


octal = 512
print("The decimal value of",octal, " is",OctalToDecimal(octal))