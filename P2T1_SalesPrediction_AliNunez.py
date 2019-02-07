# Program will predict the profit made from sales.
# 02-07-2019
# CTI 110 P2T1 - Sales Prediction
# Ali Nunez

# Get projected total sales

total_sales = float(input('Enter the projected sales:'))

# Calculate the profit as 23 percent of total sales.

profit = total_sales * 0.23

# Display the profit

print('the profit is $',format(profit, ',.2f'))
