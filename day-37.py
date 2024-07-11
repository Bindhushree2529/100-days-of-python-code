# function to convert binary to octal
def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32

    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10

        # placing current octal-sum for 3 pair in array index position
        octalArray[pos] = octalDigit

        # whenever we have read next 3 digits
        # setting values to default
        # increasing pos so next values can be placed at next array index
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1

        count += 1

    # printing octal array in reverse order
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')


binary = 1010
convert(binary)