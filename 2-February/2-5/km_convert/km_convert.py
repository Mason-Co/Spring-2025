# Programmer: Mason Colacicco
# Date: February
# Program: km Convert

# Declare Constant
KM_TO_MI = 0.6214

def main():
    # Scoping
    km = 0.0

    # User input for distance
    km = float(input("How many km should be converted?"))

    # Print miles
    show_miles(km)

def show_miles(km):
    # Scoping
    miles = 0.0

    # Calculating miles
    miles = km * KM_TO_MI
    print(f"{km} km = {miles:.2f} mi")

# Call main function
main()