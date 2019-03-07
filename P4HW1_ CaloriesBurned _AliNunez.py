# program will calculate the amount of calories burned.
# Assuming you burn 5 calories per minute when running on a treadmill,
# program will use a loop to display the number of calories burned
# after 20,35,50 minutes.
# 03-05-2019
# CTI-110 P4HW1 - Calories Burned
# Ali Nunez

# If 1 minute = 5 calories
# then 20 minutes = ?
# then 35 minutes = ?
# then 50 minutes = ?

calBurnedPerMin = 5

for numOfMin in range(20, 51, 15):
    numOfCalBurn = numOfMin  * calBurnedPerMin
    print("You will burn", numOfCalBurn,"calories in", numOfMin, "minutes.")


    
# Made a variable for calories burned per min
#   calBurnedPerMin = 5
# Made a for loop to show how many calories would be burned for each segment
# of 15 minutes:
#   20, 35, 50 minutes
# Calculations:
#   numOfCalBurn = numOfMin * calBurnedPerMin
# Displayed results of how many calories were burned for each time frame. 
