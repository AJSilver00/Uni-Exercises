
# IPDS Exercise set 1

# Testing a series of short Python programs for:
# Writing simple programs
# Simple input and output
# Using named object


# Fahrenheit to Kelvin (F to K)
# Tip: To get F to K, you need F to C then to K

fahrenheit = input("Please enter a temperature in Fahrenheit")
fahrenheit = float(fahrenheit)
celsius = ((fahrenheit - 32)/(9/5))
kelvin = celsius + 273.15
print (fahrenheit, "F converted into Kelvin, is", kelvin, "K")


# We use the following equations to get from F to C first.
# F = C x 9/5 + 32
# Rearranged to get C:
# C = ((F-32)/(9/5))

# We used this equation to get from C to K
# K = C + 273.15

