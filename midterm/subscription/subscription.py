# Programmer: Mason Colacicco
# Date: March
# Program: Subscription

def main():
    # Set constants and initialize total
    YEARS = 5
    INITIAL = total = 5000
    INTEREST = 0.05

    # Display initial value
    print(f"Initial Subscription Cost: ${INITIAL:,.2f}")

    # Loop for new value and display year
    for i in range(YEARS):
        total *= (1+INTEREST)
        print(f"Year {i+1}: ${total:,.2f}")

# Call main function
if __name__ == "__main__":
    main()