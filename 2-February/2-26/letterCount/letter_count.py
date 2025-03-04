# Programmer: Mason Colacicco
# Date: February
# Program: Letter Count

def main():
    # Initialize count and letter
    count = 0
    letter = 'a'

    # user input for name
    user_name = input("Enter your full name: ")

    # Loop through letters
    for char in user_name:
        if char.lower() == letter:
            count += 1

    # Display data
    print(f"The letter {letter.upper()} appears {count} times.")

# Call main function
if __name__ == '__main__':
    main()


