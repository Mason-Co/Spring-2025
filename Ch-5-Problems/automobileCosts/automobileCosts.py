# Programmer: Mason Colacicco
# Date: February
# Program: Automobile Costs

def main():
    # Define local variables
    loan = 0.0
    insurance = 0.0
    gasoline = 0.0
    oil = 0.0
    tires = 0.0
    maintenance = 0.0

    # User input
    loan = float(input("What is the monthly cost of loan payments? "))
    insurance = float(input("What is the monthly cost of insurance? "))
    gasoline = float(input("What is the monthly cost of gasoline? "))
    oil = float(input("What is the monthly cost of oil? "))
    tires = float(input("What is the monthly cost of tires? "))
    maintenance = float(input("What is the monthly cost of maintenance? "))

    # Call the function
    show_exp(loan,insurance,gasoline,oil,tires,maintenance)

def show_exp(debt,ins,gas,lube,rubber,maint):
    # Define local variables
    tot_month = 0.0
    tot_yr = 0.0

    # Calculate totals
    tot_month = debt + ins + gas + lube + rubber + maint
    tot_yr = tot_month * 12

    # Display data
    print(f"Monthly Expenses: ${tot_month:,.2f} \nYearly Expenses: ${tot_yr:,.2f}")


# Call main function
main()