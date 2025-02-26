# Programmer: Mason Colacicco
# Date: February
# Program: Temps

def main():
    # Initialize list and total
    temps = []
    total = 0
    for i in range(0,7):
        temp = int(input("What is the low temperature today (whole number)? "))
        temps.append(temp)
    # Calculate total and avg
    total = sum(temps)
    avg = total/7
    # Display data
    print(f"The average temperature this week was {avg:.2f}.")

# Call main function
if __name__ == '__main__':
    main()