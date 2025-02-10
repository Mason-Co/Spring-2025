# Programmer: Mason C
# Date: 1-January
# Program: Input

# Assign variables to user input
price = float(input("What is the price?"))
discountRate = float(input("What is the discount rate (decimal format)?"))
# Use user input to calculate new variables
discountAmt = price * discountRate
salesPrice = price - discountAmt

# Display data
print(f"The original price is ${price:,.2f} with a discount of {discountRate:.0%}.")
print(f"The discounted price is ${salesPrice:,.2f}.")
print(f"You saved ${discountAmt:,.2f}!")