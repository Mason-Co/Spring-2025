# Programmer: Mason Colacicco
# Date: February
# Program: Average Of Numbers

def main():
    # Read file
    infile = open(r'C:\Users\punis\PycharmProjects\Spring-2025\Chapter Problems\Ch-6-Problems\averageOfNumbers\numbers.txt', 'r')
    # Splits the numbers apart that have spaces in between them and sets them to integers
    num = [int(num) for num in infile.read().split(" ")]

    # Initialize avg
    avg = 0

    # Loop for avg
    for number in num:
        avg += number

    # Calculate avg
    avg = avg/len(num)

    # Display data
    print(f"There are {len(num)} numbers with an average of {avg:,.1f}.")


# Call main function
if __name__ == '__main__':
    main()