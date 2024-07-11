#Print N-bit binary numbers having more 1’s than 0’s in all prefixes in Python
def printRec(number, extraOnes, remainingPlaces):
    if 0 == remainingPlaces:
        print(number, end=" ")
        return

    printRec(number + "1", extraOnes + 1, remainingPlaces - 1)

    if 0 < extraOnes:
        printRec(number + "0", extraOnes - 1, remainingPlaces - 1)


def printNums(n):
    str = ""
    printRec(str, 0, n)


n = 4
printNums(n)