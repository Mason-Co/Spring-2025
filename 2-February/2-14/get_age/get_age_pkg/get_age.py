# Programmer: Mason Colacicco
# Date: February
# Program: Get Age

def main():
    try:
        # User input
        age = int(input("What is your age? "))
        # Calculate days
        day_age = age * 365

        # Display data
        print(f"{age} is {day_age} days old.")
    # Set exception
    except ValueError:
        # Show error
        print("Error: Input age as a whole number.")

# Call main function
if __name__ == '__main__':
    main()