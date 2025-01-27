# Programmer: Mason Colacicco
# Date: January
# Program: Factor

# Create Constants
HIGH = 1.5
MIDDLE = 1.25
LOW = 1.0

# User input for age and gender
age = int(input("What is your age? "))
gender = input("What is your gender (male or female)? ")

# Use age and gender to calculate factor
if gender.casefold() == "male": # Calculate male factor
    if age >= 25:
        factor = MIDDLE
    else:
        factor = HIGH
else: # Calculate female factor
    if age >= 25:
        factor = LOW
    else:
        factor = MIDDLE

# Display data
print(f"As a {gender.casefold()} at the age of {age}, your factor is {factor}.")