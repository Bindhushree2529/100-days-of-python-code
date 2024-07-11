#Hexadecimal to Decimal Conversion
def convert(hex):
    l = len(hex)
    decimal = 0
    pos = 0
    for i in range(l - 1, -1, -1):

        # if given index value is a digit (0 - 9)
        if '0' <= hex[i] <= '9':

            # if hex[i] is in range '0' - '9'
            # can convert string value to its integer value
            # by passing it to int() function
            digit = int(hex[i])
            decimal += digit * pow(16, pos)
            pos += 1

        # if given index is char in range [A, F]
        elif 'A' <= hex[i] <= 'F':

            # if hex[i] is in range 'A' - 'F'
            # can convert sting value to its int value
            # by subtracting 55(Refer Ascii table) as
            # ASCII val A: 65 and A must result 10 as value
            # to get ASCII value in Python can use ord() function
            digit = ord(hex[i]) - 55
            decimal += digit * pow(16, pos)
            pos += 1
    return decimal


hex = "C9"

print("decimal value of", hex, "is", convert(hex))