# Programmer: Mason Colacicco
# Date: February
# Program: Phone Number

def main():
    # Initialize new_number
    new_number = ''
    # User input for number
    number = input("Enter a phone number in words: ").upper()

    # Loop through each number/letter
    for char in number:
        # Replace letters
        if char.isalpha():
            if char =='A' or char == 'B' or char =='C':
                i = 2
            elif char =='D' or char =='E' or char =='F':
                i = 3
            elif char =='G' or char =='H' or char =='I':
                i = 4
            elif char =='J' or char =='K' or char =='L':
                i = 5
            elif char =='M' or char =='N' or char =='O':
                i = 6
            elif char =='P' or char =='Q' or char =='R' or char =='S':
                i = 7
            elif char =='T' or char =='U' or char =='V':
                i = 8
            else:
                i = 9
            new_number += str(i)
        # Add start numbers and other characters
        else:
            new_number += char
    # Display data
    print(f"Your new number is {new_number}!")

# Call main function
if __name__ == '__main__':
    main()