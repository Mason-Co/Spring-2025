# Programmer: Mason Colacicco
# Date: March
# Program: Interstates

def main():
    # Initialize the dictionary
    interstates = {'MN':35, 'SF':80, 'SE':90, 'WA':94, 'MI':95, 'TC':494}
    # Dynamically create new dictionaries
    eastWest = {k:v for k,v in interstates.items() if v % 2 == 0}
    important = {k:v for k,v in eastWest.items() if v % 5 == 0}

    # Display data
    print("Interstates: ")
    for i in interstates:
        print(i, ':', interstates[i])
    print("East-West:")
    for i in eastWest:
        print(i, ':', eastWest[i])
    print("Important Routes:")
    for i in important:
        print(i, ':', important[i])

# Call main function
if __name__ == '__main__':
    main()