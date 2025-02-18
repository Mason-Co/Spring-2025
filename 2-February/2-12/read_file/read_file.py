# Programmer: Mason Colacicco
# Date: February
# Program: Read File

def main():
    # Open file
    infile = open('titles.txt', 'r')

    # Read contents
    file_contents = infile.read()

    # Close file
    infile.close()

    # Print data
    print(file_contents)

# Call main function
if __name__ == '__main__':
    main()