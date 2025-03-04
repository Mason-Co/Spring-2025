# Programmer: Mason Colacicco
# Date: February
# Program: Sub Cipher

def main():
    # Initialize
    result = ''
    result2 = ''
    # User input
    msg = input("Enter a message: ")
    # Encrypt
    for i in range(len(msg)):
        char = msg[i]
        result += chr(ord(char)+3)
    # Decrypt
    for i in range(len(msg)):
        char = result[i]
        result2 += chr(ord(char)-3)
    # Display data
    print(result)
    print(result2)

# Call main function
if __name__ == '__main__':
    main()