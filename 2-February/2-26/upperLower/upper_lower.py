# Programmer: Mason Colacicco
# Date: February
# Program: Upper Lower

def main():
    # User input for sentence
    sentence = input("Enter a sentence (no spaces, each word is capitalized): ")

    # Initialize new_string and cap to skip first capital
    new_string = ""
    cap = 0

    # Loop through each letter
    # It may be inefficient, BUT I wanted to try it a little differently
    for char in sentence:
        # Skip first letter
        if cap == 0:
            cap += 1
            new_string += char.upper()
        # Create the words
        else:
            if char.isupper():
                new_string += " " + char.lower()
            else:
                new_string += char

    # Display data
    print(new_string)

# Call main function
if __name__ == '__main__':
    main()