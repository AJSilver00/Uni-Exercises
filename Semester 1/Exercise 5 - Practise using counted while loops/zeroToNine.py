# IPDS Exercise set 5
# Practise using counted while loops.

# zeroToNine
def zeroToNine ():  #alternative 1
    x=0
    while x < 10:
        print(x)
        x = x+1

# This means:
# set x to 0. While x is less than 10, display the value of x. Add 1 to x.


def zeroToNine2 (): #alternative 2
    x = 0
    while x <= 9:
        print (x)
        x = x+1

# This means:
# set x to 0. While x is less than or equal to 9, display the value of x.
# Add 1 to x.


# 1. oneToTen using while loop
def oneToTen ():
    x = 1
    while x <= 10:
        print (x)
        x = x+1

#oneToN using while loop.
def oneToN (n):
    x = 1
    while x <= n:
        print(x)
        x=x+1

#squaresToN using while loop.
def squaresToN (n):
    x = 1
    while x <= n:
        print(x)
        x = (x+1)*(x+1)  #range always starts at zero. So need to add 1 to x.
        

#repeatPrint using while loop.
def repeatPrint (s, n):
    s = str(s)
    n = int(n)
    x = 1
    while x <= n:
        print(s)
        x=x+1
        
#Power using while loop.
def power (a, b):
    a = int(a)
    b = int(b)
    p = 1                   # p = 1 because otherwise you'd have 1 too mamy
                            # multiplications
    x = 1
    while x <= b:
        p = a*p
        # Repeated multiplication of a to reach a power of a. E.g. 3,9,27,81
        x = x+1
    return(p)             # Return and loop must be in the same indentation!

#factorial using while loop.
def factorial (n):
    n = int(n)
    f = 1
    x = 1
    while x <= n:
        f = ((x+1)*f)
        x = x+1
    return(f)

#countincubes(n)
def countInCubes(n):
    counter = 1
    while counter < (n+1):
        cube = power(counter,3)
        print (cube)
        counter = counter + 1

#fibonnacci(n)
def fibonnacci(n):
    prevNum = 0
    currentNum = 1
    nextNum = 1
    counter = 1
    while counter < (n+1):
        print (currentNum)
        prevNum = currentNum
        currentNum = nextNum
        nextNum = (prevNum + currentNum)
        counter = counter + 1

#isPrime with while loop
def isPrime(n):
    n = int(n)
    c = 2
    while c <=(n):
        if c == (n):
            return True
        else:
            if n%c == 0:
                return False
            c = c+1
          
            

#isPrime with for loop
def isPrimex(n):
    n = int(n)
    for x in range (n):
        if n%(x+2) == 0:
            return ('False')
        else:
            x = x+1
            if x >= (n):
                return('True')

# define n as True if it is a prime number. False if it is not a prime number.
# Where n is an integer (only a positive number).
# for x in range n means every value up to but not including n itself.
# x is by default zero.
# assuming x = 0,
# x+2 would be 1.
# The if statement has a condition where if n modulus 1 equals 0.
# Then return the string 'False'. Loop will then end here.
# If it does not equal 0, then 1 will be added to x and the new x would be named x.
# A second nested-if condition will take place where if the new x is bigger than or equal
# to n, then the string 'True' will be returned. Loop will then end here.

#printPrimes with while loop
def printPrimes (n):
    n = int(n)
    x = 1
    while x <= n:
        if isPrime(x) == True:
            print(x)
        x = x+1
        
#printPrimes for loop
def printPrimesx(n):
    n = int(n)
    for x in range (n):
        a=x+1
        if isPrime(a) == True:
            print(a)
        x = x+1

# define n as the print of all prime numbers.
# Where n is an integer (only positive number)
# for x in range n means every value up to but not including n itself.
# x is by default zero.
# we add 1 to x and call it a. Because we want it to start counting from 1.
# if isPrime(a) is True, then a will be printed. Then we add 1 again to x and call it x.
# the range loop will be repeated now with the new x.
# If we call printPrimes(12), it will print all the possible prime numbers between 1 and 12.

#printFactors with while loop
def printFactors(n):
    n=int(n)
    x=1
    while x <= n:
        if n%x == 0:
            print(x)
        x = x+1
    
# if n/x then x is factor of n.
# n is an integer (only positive number)
# x equals 1.
# While 1 is less than or equal to n, if the remainder of n/x = 0, print x.
# Then add 1 to x and call it x.
# The new x will therefore equal 2.
# The while loop will be repeated using x=2 and keep repeating until n is reached.

#printFactors with for loop.
def printFactorsx(n):
    n = int(n)
    for x in range (n):
        if n%(x+1) == 0:        # it is x+1 because we want to start count from 1.
            print(x+1)           # why return with for loop and not print??????


#printPrimefactors with while loop.
def printPrimeFactors(n):
    n = int(n)
    y = n
    x = 2
    while x <= n:
        if isPrime(x) == True:
            if y%x == 0:
                print(x)
                y = y/x
            else:
                x = x+1
        else:
            x = x+1

#printPrimeFactors using for loop.
def printPrimeFactorsx(n):
    n = int(n)
    y = n
    for x in range (n-1):
        if isPrime(x+2) == True:
            if y%(x+2) == 0:
                print(x+2)
                y = y/(x+2)
            else:
                x = x+1
        else:
            x = x+1

# Practice using an uncounted (but definite) while loop
def gcd(a,b):
    a = int(a)
    b = int(b)
    y = b
                        #    a = b(x) + (y)
                        #    b = b//y + b%y    # // = floor operator
    while y > 0 :
        x = a//b
        y = a%b
        if y == 0:
            print('GCD =', b)
        else:
            a = b
            b = y

# Practice using indefinite while loops.
def mean():
    total = 0               #print = (input('Please type in a series of numbers'))
    n = 0
    goAgain = 'yes'
    while goAgain == 'yes':
        num_str = input('Please type in a number')
        number = int(num_str)
        total = total + number
        n = n + 1
        goAgain = input('Do you want to enter another?')
    mean = total/n
    print ('The mean of the numbers you entered is', mean)

def mean1():
    total = 0
    n = 0
    stop = 'no'
    while stop != 'yes':
        num_str = input('Please type in a number')
        number = float(num_str)
        total = total + number
        n = n+1
        stop = input('Do you want to stop?')
    mean = total/n
    print('The mean of the numbers you entered is', mean)

def mean2():
    total = 0
    n = 0
    while True:
        num_str = input('Please type in a number')
        number = float(num_str)
        total = total + number
        n=n+1
        stop = input('Do you want to stop?')
        if stop == 'yes':
            break
    mean = total/n
    print('The mean of the numbers you entered is', mean)

def mean3():
    total = 0
    n_str = input ('How many numbers do you want to enter?')
    n = int(n_str)
    count = 0
    while count < n:
        num_str = input('Please type in a number')
        number = float(num_str)
        total = total + number
        count = count+1
    mean = total/n
    print('The mean of the numbers you entered is', mean)
            
# positives
def positives ():
    total = 0
    n = 0
    while True:
        num_str = input('Please type in a number')
        number = float(num_str)
        if number > 0:
            n = n+1
        else:
            n = n
        stop = input('Do you want to stop?')
        if stop == 'yes':
            break
    print('In the list of numbers you have entered, ', n, 'of them are positive')
                    
            
# signs
def signs ():
    total = 0
    p = 0
    n = 0
    z = 0
    while True:
        num_str = input('Please type in a number')
        number = float(num_str)
        if number > 0:
            p = p + 1
        elif number < 0:
            n = n + 1
        else:
            z = z + 1
        stop = input('Do you want to stop?')
        if stop == ' yes':
            break
    print('In the list of numbers you have entered, ', p, 'of them are positive.', n, \
          'of them are negative and', z, 'of them are zero')

# greatest
def greatest():
    total = 0
    lst = []
    n_str = input ('How many numbers do you want to enter?')
    n = int(n_str)
    count = 0
    while count < n:
        num_str = input('Please type in a number')
        number = float(num_str)
        lst.append(number)
        count = count+1
    print('Out of the numbers you entered,', max(lst), 'is the greatest')

# longest of all
def longestOfAll():
    lst = []
    n_str = input ('How many strings do you want to enter?')
    n = int(n_str)
    count = 0
    while count < n:
        s_str = input('Please type in a string')
        s_str = str(s_str)
        lst.append(s_str)
        count = count+1
    longest = max(lst, key=len)
    print('Out of the strings you entered,', longest, 'is the longest string')


# more challenging exercises

# days between
#def daysBetween():







   
