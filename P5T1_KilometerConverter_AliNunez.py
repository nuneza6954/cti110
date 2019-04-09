# The program will convert the distance kilometers to miles. 
# 03-26-2019
# CTI-110 P5T1_KilometerConverter 
# Ali Nunez

# This prgram converts kilometers to miles.
conversion_factor = 0.6214

# The main function gets a distance in kiolmeters and calls
# the show_miles function to convert it.
def main():
    # Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # display the distance converted to miles.
    show_miles(kilometers)

# The show_miles funstion converts to the parameter km from
# kilometers to  miles and displays the result. 

def show_miles(km):
    # Calculate miles.
    miles = km * conversion_factor

    # Display the miles.
    print(km, 'kilometers equals', format(miles, '.2f'), "miles.")


# Call the main functions
main()
