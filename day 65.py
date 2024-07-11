#Find all possible Palindromic Partitions of the given String in Python
def isPalindrome(str, low, high):
    while low < high:
        if str[low] != str[high]:
            return False
        low += 1
        high -= 1
    return True


def allPalPartUtil(allPart, currPart, start, n, str):

    if start >= n:
        x = currPart.copy()
        allPart.append(x)
        return

    for i in range(start, n):
        if isPalindrome(str, start, i):
            currPart.append(str[start:i + 1])
            allPalPartUtil(allPart, currPart, i + 1, n, str)
            currPart.pop()


def allPalPartitions(str):

    n = len(str)
    allPart = []
    currPart = []
    allPalPartUtil(allPart, currPart, 0, n, str)

    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j], end=" ")
        print()


string = "nitin"
allPalPartitions(string)