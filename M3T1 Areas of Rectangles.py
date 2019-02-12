# The program will ask for the length and width of two rectangles.
# Program will find the area of two rectangles. 
# 02-12-2019
# CTI-110 - Tutorial - P3T1 - Areas of Rectangles
# Ali Nunez

# Input variables
# Get dimensions of rectangle 1.
L1 = int(input('Enter the length of rectangle 1: '))
W1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions for ectangle 2. 
L2 = int(input('Enter the length of rectangle 2: '))
W2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of the rectangles.
area1 = L1 * W1
area2 = L2 * W2

# Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
    



