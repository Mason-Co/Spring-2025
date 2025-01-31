# Programmer: Mason Colacicco
# Date: January
# Program: Average Rainfall

# User input for years and initialize rain
years = int(input("Number of years to calculate: "))
rain = 0

# Initial loop for the years
for i in range(0,years):
    for m in range(0,12): # Nested loop for each month
        rain += float(input(f"Inches of rainfall in month {m+1}: "))

# Calculate months and average
months = years*12
avg = rain/months

# Display data
print(f"In {years} year(s) over {months} months, there was a total of {rain:,.1f} inches of rain.")
print(f"The average rainfall each month was {avg:.1f} inches.")