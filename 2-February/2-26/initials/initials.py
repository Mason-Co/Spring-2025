# Programmer: Mason Colacicco
# Date: February
# Program: Initials

def main():
    # Initialize initials
    initials = ''

    # User input for name, then split it
    user_name = input("Enter your full name: ")
    parts = user_name.split()

    # Loop for initials
    for word in parts:
        initials += word[0].upper() + '.'

    # Display data
    print(initials)

# Call main function
if __name__ == '__main__':
    main()