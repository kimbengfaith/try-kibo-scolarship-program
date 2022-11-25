# Write your solution below
# Follow the instructions in the tab to the right
# enter your ammount in US Dollars
us_dollars=float(input("enter your amount in us dollars: "))
# Use this exchange rate
NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021
# Assigning the values of both us_dollars and NAIRA_PER_DOLLAR to USD and NGN respectively
USD=us_dollars
NGN=NAIRA_PER_DOLLAR
# converting USD to NGN and storing in NGN
NGN = USD * NGN
# print out the value of NGN to 2 decimal places
print(f"the amount in Nigerian Naira is: {round(NGN,2)}")