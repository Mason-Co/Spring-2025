# Programmer: Mason Colacicco
# Date: February
# Program: Future Value

def main():
    # Define variables
    p = float(input("What is the present value? "))
    i = float(input("What is the interest rate (decimal format)? "))
    t = int(input("How many months will pass? "))

    # Call interest function
    f = interest(p,i,t)

    # Display data
    print(f"The future value is ${f:,.2f} in {t} months.")

def interest(value,rate,months):
    # Calculate future value
    return value*(1+rate)**months


# Call main function
if __name__ == '__main__':
    main()