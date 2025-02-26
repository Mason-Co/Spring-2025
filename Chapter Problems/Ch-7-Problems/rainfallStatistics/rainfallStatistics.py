# Programmer: Mason Colacicco
# Date: February
# Program: Rainfall Statistics

def main():
    # Initialize rainfall list
    rainfall = []

    # Loop for rainfall
    for i in range(12):
        rainfall.append(int(input(f"What was the rainfall in month {i+1} (inches)? ")))

    # Calc total, avg, max, min
    total = sum(rainfall)
    avg = total / 12
    maxi = max(rainfall)
    mini = min(rainfall)

    # Display data
    print(f"Total Rainfall: {total} \nAverage Rainfall: {avg:.2f} \nHighest Rainfall: {maxi} \nLowest Rainfall: {mini}")


# Call main function
if __name__ == "__main__":
    main()