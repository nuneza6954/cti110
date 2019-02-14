# CTI-110 
# P3HW1 - Color Mixer 
# Ali Nunez
# 02-14-2019
# Program will prompt the user to enter the names of two primary colors to mix
# If the user enters anything other than "red", "blue", or "yellow", the program
# should display an error message. Otherwise,the program should display the name
# of the secondary color that results.

# Input variables

primaryColor1 = input("Please enter primary color 1: " )
primaryColor2 = input("Please enter primary color 2: " )

# Prompt the user

print()

if ( primaryColor1 == "red" and primaryColor2 == "blue" ) or \
   ( primaryColor1 == "blue" and primaryColor2 == "red" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is purple")
elif ( primaryColor1 == "red" and primaryColor2 == "yellow" ) or \
     ( primaryColor1 == "yellow" and primaryColor2 == "red" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is orange")
elif ( primaryColor1 == "blue" and primaryColor2 == "yellow" ) or \
     ( primaryColor1 == "yellow" and primaryColor2 == "blue" ):
     print( primaryColor1 + " mixed with " + primaryColor2 + " is green")
else:
    print( "At least one of your colors, " + primaryColor1 + " or " + \
           primaryColor2 + ", is not a primaryColor" )

# Got information from user
# You have two Primary Colors, primaryColor1 and primaryColor2
# Prompt the user to ask us to input those Primary Colors
#   Input Variables
# Make different variations of combinations available
#   Prompt the user to enter in colors
#   primaryColor1 + primaryColor2 = Color Mix
# User will prompt if any other variations of color is NOT a primaryColor 


