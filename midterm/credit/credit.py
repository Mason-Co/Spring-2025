# Programmer: Mason Colacicco
# Date: March
# Program: Credit Card Account Verification

def main():
    try:
        # Open, read to a list, and close file
        infile = open("credit_card.txt", 'r')
        verif_str = infile.read().split('\n')
        infile.close()
        # Initialize verification list of numbers
        verification = []

        # User input for credit card number
        user_card = int(input("Enter your credit card number: "))

        # Loop for list to be number
        for num in verif_str:
            verification.append(int(num))

        # Check for credit card
        if user_card not in verification:
            print("Your credit card number is not in the list.")
        else:
            print("Your credit card number is in the list.")

    except ValueError:
        # Error if credit card is not a number
        print("Invalid credit card number.")


# Call main function
if __name__ == "__main__":
    main()