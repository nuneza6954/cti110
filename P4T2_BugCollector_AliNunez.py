# This program will loop for the number of (5)days, program will prompt the
# user to ask it how many bugs have been collected for each day, and when
# the loop is finished, the prgram should display the total number
# of bugs collected.
# 03-05-2019
# CTI-110 P4T2 - Bug Collector
# Ali Nunez

# Set total = 0
# for each of 5 days:
#   Input bugs collected for a day
#   Add bugs collected to total
# Display total

# Initialize the accumulator.

total = 0

# Get the bugs collected for each day.

for day in range(1,6):
    # Prompt the user
    print('Enter the bugs collected on day', day)
    
    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total
    total = total + bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
    
