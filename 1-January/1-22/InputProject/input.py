# Programmer: Mason C
# Date: 1-January
# Program: Input

# Assign variables to user input
name  = input("Name: ")
age = int(input("Age: "))
income = float(input("Income: "))

# Display variables
print(f"Your name is: {name}")
print(f"Your age is: {age}")
print(f"Your income is: ${income:,.2f}")