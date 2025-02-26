# Programmer: Mason Colacicco
# Date: February
# Program: Random Number File Writer

from random import randint

def main():
    # User input for amount of numbers
    count = int(input("How many numbers do you want to generate? "))

    # Open file to write
    outfile = open('randomNumbers.txt', 'w')

    # Loop for random numbers and writing them separated by a space
    for i in range(count):
        outfile.write(f"{str(randint(1, 500))} ")

    # Close file
    outfile.close()


# Call main function
if __name__ == '__main__':
    main()