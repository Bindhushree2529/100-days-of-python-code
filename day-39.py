#Python program to find out the quadrant in which the given co-ordinate lie
# for initialization of coordinates
x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))

# find true condition of first quadrant
if x > 0 and y > 0:
    print("point (", x, ",", y, ") lies in the First quadrant")

# find second quadrant
elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")

# To find third quadrant
elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")
 # To find Fourth quadrant 
elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant")

# To find does not lie on origin
elif x == 0 and y == 0:
    print("point (", x, ",", y, ") lies at the origin")

# On x-axis
elif y == 0 and x != 0:
    print("point (", x, ",", y, ") on x-axis")

# On y-axis
elif x == 0 and y != 0:
    print("point (", x, ",", y, ") on at y-axis")