#Octal To Binary Conversion
def convert(octal):
    i = 0
    decimal = 0
    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(8, i)
        octal //= 10
        i += 1
    print("Decimal Value :", decimal)
    binary = 0
    rem = 0
    i = 1

    while decimal != 0:
        rem = decimal % 2
        decimal //= 2
        binary += rem * i
        i *= 10
    print("Binary Value :", binary)


octal = int(input("Octal Value : "))
convert(octal)
