#decimal to octal conversion
decimal = 148
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")