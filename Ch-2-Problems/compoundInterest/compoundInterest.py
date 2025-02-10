# Programmer: Mason Colacicco
# Date: 1-January
# Program: Compound Interest

# User input for variables
p = float(input("What is the principle amount deposited? "))
r = float(input("What is the annual interest rate (decimal format)? "))
n = int(input("How many times per year is interest compounded? "))
t = int(input("What is the number of years interest will accrue? "))
# Calculate final total
rn = r/n
nt = n*t
a = p*((1+rn)**nt)

# Display data
print(f"There will be ${a:,.2f} after {t} years.")