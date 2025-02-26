# Programmer: Mason Colacicco
# Date: February
# Program: Sales

def main():
    # Initialize week index
    ind = 1
    # Initialize week numbers
    week1 = [250,220,320,190,250]
    week2 = [240,200,315,200,260]
    week3 = [230,210,300,230,275]
    week4 = [260,220,315,225,290]
    weeks = [week1,week2,week3,week4]

    # Loop for totals
    for week in weeks:
        # Reset total
        total = 0
        for day in week:
            total += day
        # Display data
        print(f"Week {ind}: ${total:.2f}")
        # Increment week number
        ind += 1

# Call main function
if __name__ == "__main__":
    main()