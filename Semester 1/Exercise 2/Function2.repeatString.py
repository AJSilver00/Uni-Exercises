# IPDS Exercise set 2
# Functions without parameters - In this exercise set, we learn how to
# define functions.
# Using the same answers I have given to exercise set 1, I will give  a
# title/def/name to the Python Program that I will execute.

# Repeating Strings

def repeatString ():
    theString = input ("Please enter a character string")
    num = input ("Please enter in a positive whole number")
    num = int(num)                  #This step is converting the string num
                                    #into integer and then storing the
                                    #result back into num.
    multiString = (theString * num) #This will repeat theString num times.
                                    #Like so:
    print (multiString)         
