# Programmer: Mason Colacicco
# Date: January
# Program: Pennies for Pay

# User input for days and set initial pay
days = int(input("How many days of pay are there? "))
pay = 0.01

# Header of table
print("Day\tPay\n---------")

# Loop to calculate pay and create table
for i in range(0,days):
    print(f"{i+1}\t${pay}")  # Display data
    pay *= 2  # Double pay