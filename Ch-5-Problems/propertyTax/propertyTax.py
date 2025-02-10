# Programmer: Mason Colacicco
# Date: February
# Program: Property Tax

# Create Global Constants
ASSESS_PERCENT = 0.60
PROP_TAX_PERCENT = 0.73

def main():
    # User input
    value = float(input("What is the actual value of the property? "))

    # Call show prop tax function
    show_prop_tax(value)

def show_prop_tax(num):
    # Call global variables
    global ASSESS_PERCENT
    global PROP_TAX_PERCENT

    # Calculate
    assessment = num * ASSESS_PERCENT
    taxes = (assessment//100) * PROP_TAX_PERCENT

    # Display data
    print(f"Assessment Value: ${assessment:,.2f}\nProperty Tax: ${taxes:,.2f}")


# Call main function
main()