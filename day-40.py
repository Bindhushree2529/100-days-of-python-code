#Python Program for Permutations In Which N People Can Occupy R Seats In A Classroom
# Permutations in which n people can occupy r seats

# function for factorial
def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact


# main program
# user input
n = int(input("Enter number of people: "))
r = int(input("Enter number of seats: "))

# finding all possible arrangements of n people on r seats
# by using formula of permutation
p = factorial(n) // factorial(n - r)

# printing output
print("Total possible arrangements:", p)