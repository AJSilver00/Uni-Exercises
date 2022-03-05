# IPDS Exercise 3

# Functions that make use of for loops to print a sequence of values.

# 1. Example: print the whole numbers from zero to nine
def zeroToNine ():
    for x in range (10):
        print(x)

# 2. Print the whole numbers from one to ten
def oneToTen ():
    for x in range (10):
        print(x+1)

# 3. Print whole numbers from one to n
def oneToN (n):
    for x in range (n):
        print(x+1)

# 4. Print the squares of the whole numbers from one to n
def squaresToN (n):
    for x in range (n):
        print((x+1)*(x+1))  #range always starts at zero. So need to add 1 to x.

# 5. Print a string several times over
def repeatPrint (s, n):
    s = str(s)
    n = int(n)
    for x in range (n):
        print(s)
        
# 6. Raise a number to a power
def power (a, b):
    a = int(a)
    b = int(b)
    p = 1                  # p = 1 because otherwise you'd have 1 too mamy multiplications
    for x in range (b):
        p = a*p            # Repeated multiplication of a to reach a power of a. E.g. 3,9,27,81
    return (p)             # Return and for loop must be in the same indentation!

# 7. Calculate factorials
def factorial (n):
    n = int(n)
    f = 1
    for x in range (n):
        f = ((x+1)*f)
    return (f)


