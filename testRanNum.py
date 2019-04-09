# Program will generate a random number 1-100 using def and or a while loop
# and the program will either deny or accept that the user has guessed the
# correct number. Program will also keep count of the number of guesses. 
# 03-27-2019
# CTI-110 P5HW1 - Random Number
# Ali Nunez


def testRanNum():

    import random

    ranNum = random.randint(1, 101)

    #print(ranNum)

    guess = 0
    tries = 0
  
    while guess != ranNum:
        guess = int(input( "Guess a number: "))
        tries = tries + 1
        
        if guess > ranNum:
            print( "Too high, Try Again: ")
        elif guess < ranNum:
            print ( "Too Low, Try Again: ")
        else:
            print()
            print("Congratulations! You guessed correctly the number was",\
                  + ranNum)
            print("Number of tries:", tries)


prompt = 'yes'
while prompt == 'yes':
    testRanNum()
    print()
    
    prompt = input("Do you want to play again? Enter Yes or No: ")
    if prompt == 'no':
        print("GoodBye!")


# Defined this program as testRanNum
# Imported a random number to be generated and called it ranNum
# Declared my variables
#       guess = 0
#       tries = 0
# Created a while loop that would prompt the user to guess a number
# Program would tell the user if they are guessing too high or too low
# If guessed correctly the user will be congratulated
# Program will display the correct number guessed and how many tries were made
# Then the user is asked if they want to play again
# If yes, program will run again by calling this file and starting it over
#   while prompt == 'yes'
#       testRanNum()
# If no, the program will say "GoodBye"












