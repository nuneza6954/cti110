# Program will convert feet to inches.
# 03-26-2019
# CTI-110 P5T2_FeetToInches 
# Ali Nunez


# Constant for the number of inches per foot
inches_per_foot = 12


# main function
def main():
    # Get a number of feet from the user
    feet =  int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches. 
def feet_to_inches(feet):
    return feet * inches_per_foot


# Call the main function.
main()
                
