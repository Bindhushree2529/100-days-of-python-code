#Find the Nth row in Pascal’s Triangle in Python
def getrow(N):
    prev = 1
    print(prev, end=" ")

    for i in range(1, N + 1):
        curr = (prev * (N - i + 1)) // i
        print(curr, end=" ")
        prev = curr


N = 2
getrow(N)