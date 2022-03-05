
# IPDS Exercise set 2
# Functions without parameters - In this exercise set, we learn how to
# define functions.
# Using the same answers I have given to exercise set 1, I will give  a
# title/def/name to the Python Program that I will execute.

def FtoC ():
    fahrenheit = input("Please enter a temperature in Fahrenheit")
    fahrenheit = float(fahrenheit)
    celsius = ((fahrenheit - 32)/(9/5))
    print (fahrenheit, "F converted to degrees Celsius will be", celsius, \
                       "degrees Celsius")

#In order to calculate celsius, the following equation was used:
# F = C x 9/5 + 32

# I rearranged this equation to find celsius:
# C = (F-32)/(9/5)

