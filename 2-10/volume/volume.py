# Programmer: Mason Colacicco
# Date: February
# Program: Volume

def main():
    # User input
    box_height = float(input("Height of box in inches: "))
    box_width = float(input("Width of box in inches: "))
    box_length = float(input("Length of box in inches: "))

    # Call volume function
    box_volume = volume(box_height,box_width,box_length)

    # Display data
    print(f"Volume: {box_volume:,.1f} in^3")

def volume(height,width,length):
    # Calculate and return volume
    vol = height*width*length
    return vol

# call main function
if __name__ == "__main__":
    main()