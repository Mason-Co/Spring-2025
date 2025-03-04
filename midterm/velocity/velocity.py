# Programmer: Mason Colacicco
# Date: March
# Program: Velocity

def main():
    # Set constants
    DISTANCE = 26.2
    TIME_HOUR = 3
    TIME_MINUTE = 16

    # Calculate times
    total = TIME_HOUR * 60 + TIME_MINUTE
    av_minute = int(total//DISTANCE)
    av_second = (total/DISTANCE - av_minute) * 60

    # Display data
    print(f"The average mile time was {av_minute}:{av_second:.0f}.")

# Call main function
if __name__ == '__main__':
    main()