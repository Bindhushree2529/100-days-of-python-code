#Decimal to Hexadecimal Conversion
def convert(num):
    hexa = []

    while num != 0:

        rem = num % 16

        if rem < 10:
            hexa.append(chr(rem + 48))
        else:
            hexa.append(chr(rem + 55))
        num = num // 16

    hexa.reverse()
    return ''.join(hexa)


decimal = 2545
print("Hexadecimal :", convert(decimal))