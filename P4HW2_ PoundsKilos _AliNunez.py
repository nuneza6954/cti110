# Program will display a table of pounds starting from 100 through 300
# (with a step value of 10) and their equivalent kilograms.
# The formula for converting pounds to kilograms is:
#   kg= lb/2.2046
# Program will do a loop to display the table.
# 03-07-2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Ali Nunez

# Declare Variables

pounds = 0
kilogram = 0

# Get input from user

pounds = float(input("Enter weight in pounds:"))

# Calculation: convert pounds to kilograms

kilogram =  pounds/2.2046

for pounds in range(100, 300, 10):
    kilogram = pounds / 2.2046
    print("Pounds:", pounds, " Kilograms:" ,format(kilogram,'.2f'),sep="")

# Declared my variables
#   pounds = 0
#   kilogram = 0
# Prompt user for input to "Enter weight in pounds"
# Used a calculation to pounds to kilograms
#   kilogram = pounds / 2.2046
# Displayed conversion for every tenth value strarting at 100 to 300
# using a for loop. 
