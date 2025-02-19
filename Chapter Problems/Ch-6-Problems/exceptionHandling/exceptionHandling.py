# Programmer: Mason Colacicco
# Date: February
# Program: Exception Handling

def main():
    # Error Trap
    try:
        # Read file
        infile = open(r'C:\Users\punis\PycharmProjects\Spring-2025\Chapter '
                      r'Problems\Ch-6-Problems\exceptionHandling\numbers.txt', 'r')
        # Splits the numbers apart that have spaces in between them and sets them to integers
        num = [int(num) for num in infile.read().split(" ")]

        # Close file
        infile.close()

        # Initialize avg
        avg = 0

        # Loop for avg
        for number in num:
            avg += number

        # Calculate avg
        avg = avg/len(num)

        # Display data
        print(f"There are {len(num)} numbers with an average of {avg:,.1f}.")

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')


# Call main function
if __name__ == '__main__':
    main()