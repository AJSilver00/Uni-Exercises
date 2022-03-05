
# IPDS Exercise set 1

# Testing a series of short Python programs for:
# Writing simple programs
# Simple input and output
# Using named object


# Calculating years and months from months

totalMonths = input ("Please enter a whole number")
totalMonths = int(totalMonths)
years = (totalMonths // 12)
months = totalMonths % 12
print (totalMonths, "months is", years, "years and", months, "months")


# Python's integer division operation // should be
# used to get the number of years.
# // means floor division. E.g. 0.999 will equal 0.
# Python's remainder operation % should be used to get the remaining months.
