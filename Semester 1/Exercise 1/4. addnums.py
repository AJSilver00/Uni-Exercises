

# IPDS Exercise set 1

# Testing a series of short Python programs for:
# Writing simple programs
# Simple input and output
# Using named object


# Second example: a program to add two numbers

num1 = input("Please type in a whole number")           #step 1
num2 = input("Please type in another whole number")     #step 2
num1 = int(num1)                                        #step 3
num2 = int(num2)                                        #step 4
total = num1 + num2                                     #step 5
print (num1, "+", num2, "is", total)                    #step 6

#What happens if you leave out the code that implements steps 3 and 4?

num1 = input("Please type in a whole number")           #step 1
num2 = input("Please type in another whole number")     #step 2
                                                        #deleted step
                                                        #deleted step
total = num1 + num2                                     #step 5
print (num1, "+", num2, "is", total)                    #step 6

# If you leave out steps 3 and step 4,
# Then step 5 will just concatenate num1 and num2.
# Computer will print out: 3 +  4 is 34
# Because it is simply 'glueing' numbers together.
# If you want it to print: 3 + 4 is 7,
# Then you MUST define num1 and num2 as integers.
# Only that way will the computer treat num1 and num2 as int rather than str.

