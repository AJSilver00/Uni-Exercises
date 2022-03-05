
# IPDS Exercise set 1

# Testing a series of short Python programs for:
# Writing simple programs
# Simple input and output
# Using named object


# Currency conversion

euro = input("Please enter how many Euros can be bought for 1 pound")
euro = float(euro)
hundredEuro = 100/euro
print("£",hundredEuro, "will be the cost for 100 Euros")

euroBuy = input("Please enter how many Euros you would like to buy")
euroBuy = float(euroBuy)
buy = euroBuy/euro
print ("£",buy, "will be the cost for", euroBuy, "Euros")

