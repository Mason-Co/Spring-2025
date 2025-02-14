# Programmer: Mason Colacicco
# Date: 1-January
# Program: Total Purchase

# Set variables and ask for item price
subTotal = 0.0
for i in range(0,5):
    price = float(input(f"what is the price of item {i+1}?"))
    # Add each price to the total
    subTotal += price
# Calculate remaining variables
tax = subTotal * 0.07
total = tax + subTotal

# Display data
print(f"Subtotal: ${subTotal:,.2f}\nSales Tax: ${tax:,.2f}\nTotal Cost: ${total:,.2f}")