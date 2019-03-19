# Program will use a loop that asks the user to enter in a series of positive
# numbers. The user should enter a negative number to signal the end of the
# series. After all the positive numbers have been entered, the program should
# display their sum. 
# March 19, 2019
# CTI-110 P4HW3 - Sum of Numbers
# Ali Nunez

total  = 0
userNum = float( input("Please enter the first number or a negative " + \
                       "number to quit: "))

while userNum > -1:
    total = total + userNum
    userNum = float( input("Please enter the next number or a negative " + \
                           "number to quit: "))

print()
print("The sum of all the number you entered is" , total)

# Showed my variables
#  total = 0 , userNum
# Prompt user to enter in the number that will be adding up or a negative number
# to quit the program and add the total
# Created a while loop that will conintue to run until a negative number
# is entered, once a negative number is entered it will calucalte the sum of
# positive numbers using:
#   total = total + userNum
# Displayed the sum of all numbers


