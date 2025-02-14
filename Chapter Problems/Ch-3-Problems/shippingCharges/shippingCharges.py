# Programmer: Mason Colacicco
# Date: 1-January
# Program: Shipping Charges

# Constants
LIGHT = 1.5
MEDIUM = 3.0
HEAVY = 4.0
HEAVIEST = 4.75

# User input for weight
weight = int(input("What is the weight of the package (lb)?"))

# Determine shipping rate
if weight <= 2:
    rate = LIGHT
elif weight <= 6:
    rate = MEDIUM
elif weight <= 10:
    rate = HEAVY
else:
    rate = HEAVIEST
# Determine total
total = rate * weight

# Display data
print(f"A weight of {weight} lb will cost ${rate} per lb.\nThe total cost is ${total:,.2f}.")