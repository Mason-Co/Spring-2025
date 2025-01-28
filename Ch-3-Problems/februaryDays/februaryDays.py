# Programmer: Mason Colacicco
# Date: January
# Program: February Days

# User input for year
year = int(input("What year will be checked? "))

# Determine Leap year
if year % 100 != 0 and year % 4 == 0:
    days = 29
elif year % 400 == 0 and year % 100 == 0:
    days = 29
else:
    days = 28

# Display data
print(f"In {year} February has {days} days.")