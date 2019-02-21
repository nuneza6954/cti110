# CTI-110 
# P3HW2 - MealTipTax 
# Ali Nunez
# 02-19-2019


meal = float(input("Enter total amount of meal:$"))


tip15 = meal * .15
tip18 = meal * .18
tip20 = meal * .20

salesTax = 0.07 * meal

total15 = meal + tip15 + salesTax
total18 = meal + tip18 + salesTax
total20 = meal + tip20 + salesTax

tip = float(input("Enter tip percentage: %"))

if(tip == 15):
    print("Meal Charge: $" + format( meal, ",.2f"), \
      "Tip: $" + format( tip15, ",.2f" ), \
      "SalesTax: $"  + format( salesTax, ",.2f"), \
      "Total: $" + format( total15, ",.2f"), sep = "\n" )
elif(tip == 18):
    print("Meal Charge: $" + format( meal, ",.2f"), \
      "Tip: $" + format( tip18, ",.2f" ), \
      "SalesTax: $"  + format( salesTax, ",.2f"), \
      "Total: $" + format( total18, ",.2f"), sep = "\n" )
elif(tip == 20):
    print("Meal Charge: $" + format( meal, ",.2f"), \
      "Tip: $" + format( tip20, ",.2f" ), \
      "SalesTax: $"  + format( salesTax, ",.2f"), \
      "Total: $" + format( total20, ",.2f"), sep = "\n" )
else:
    print("ERROR")


# Declared my Variables
# Declared my Calculations
# Prompt the user to ask for the Total Amount of the meal
# Prompt the user to ask for the correct tip percentage
#   If correct precentage is entered: 15%, %18, or %20
#       Program will continue to display the rest of the bill
#   If different percentage is entered:
#       The program will display an "ERROR" message







