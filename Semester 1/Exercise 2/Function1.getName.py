
# IPDS Exercise set 2
# Functions without parameters - In this exercise set, we learn how to
# define functions.
# Using the same answers I have given to exercise set 1, I will give  a
# title/def/name to the Python Program that I will execute.


#E.g. In exercise 1 set 1, I gave this answer:
#forename = input ("Please enter your forename")
#country = input ("Please enter the country where you were born")
#print (forename, "was born in", country)

#Now in exercise 1 set 2, I am giving this answer:
def bornIn ():
    forename = input ("Please enter your forename")
    country = input ("Please enter the country where you were born")
    print (forename, "was born in", country)

# The only difference between exercise 1 and exercise 2 is that, in exercise 2
# I am defining the Python Program now as a Python Function where I can now
# name my own python program, which is great!

# Concatenating strings ->

def getName ():     # This line is defining this python program as 'getName'.
    forename = input("Please enter your forename")
    surname = input("Please enter your surname")
    fullname = (forename + surname)
    print (fullname)


# In order to run a function program, simply type the following in the
# Python terminal:
# e.g. bornIn()
# or can type getName()
