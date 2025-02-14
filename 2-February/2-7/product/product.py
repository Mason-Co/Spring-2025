# Programmer: Mason Colacicco
# Date: February
# Program: Product

def main():
    # Get user input
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))

    # Call calc function
    calc(x, y)

def calc(num1, num2):
    # Print data
    print(f"Your product is: {num1 * num2}")

# Call main function
main()