# Programmer: Mason Colacicco
# Date: February
# Program: Item Counter

def main():
    # Open and read the file lines
    infile = open('names.txt', 'r')
    file_contents = infile.readlines()

    # Initialize Count
    line_count = 0

    # Loop for count
    for lines in file_contents:
        line_count += 1

    # Display data
    print(f"there are {line_count} lines in the file.")

# Call main function
if __name__ == '__main__':
    main()